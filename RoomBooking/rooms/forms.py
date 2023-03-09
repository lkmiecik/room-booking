from django.forms import ModelForm, CharField, IntegerField, BooleanField, ModelChoiceField, DateField, TimeField
from django.core.exceptions import ValidationError
from .models import Building, Room, ReservingPerson, Reservation
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


def zip_code_validator(value):
    error_message = "Niepoprawny kod pocztowy"
    if len(value) > 6 or len(value) < 5:
        raise ValidationError(error_message)
    if len(value) == 5:
        for c in value:
            if not c.isdigit():
                raise ValidationError(error_message)
    if len(value) == 6:
        for i in range(len(value)):
            if i == 2 and value[i] != "-":
                raise ValidationError(error_message)
            if i != 2 and not value[i].isdigit():
                raise ValidationError(error_message)


def time_validator(value):
    if value.minute % 15 != 0:
        raise ValidationError("Wymagana gradacja czasu to 15 minut")


class BuildingForm(ModelForm):
    number = CharField(label='Numer')
    street = CharField(label='Ulica')
    town = CharField(label='Miasto')
    zip_code = CharField(label='Kod pocztowy', validators=[zip_code_validator])

    class Meta:
        model = Building
        fields = '__all__'


class RoomForm(ModelForm):
    number = CharField(label='Numer')
    area = CharField(label='Powierzchnia w m2')
    building = ModelChoiceField(label='Budynek', queryset=Building.objects.all())
    floor = IntegerField(label='Piętro')
    capacity = IntegerField(label='Liczba miejsc')
    equipment = CharField(label='Wyposażenie')
    accessibility = BooleanField(label='Dostępność dla niepełnosprawnych')

    class Meta:
        model = Room
        fields = '__all__'


class ReservingPersonForm(ModelForm):
    name = CharField(label='Imię')
    surname = CharField(label='Nazwisko')

    class Meta:
        model = ReservingPerson
        fields = '__all__'


class ReservationForm(ModelForm):
    room = ModelChoiceField(label='Sala', queryset=Room.objects.all())
    reserving_person = ModelChoiceField(label='Rezerwujący', queryset=ReservingPerson.objects.all())
    date = DateField(label='Data', widget=DateInput)
    start_time = TimeField(label='Godzina rozpoczęcia', widget=TimeInput, validators=[time_validator])
    end_time = TimeField(label='Godzina zakończenia', widget=TimeInput, validators=[time_validator])

    class Meta:
        model = Reservation
        fields = '__all__'

    def overlap(self, min1, max1, min2, max2):
        return max(0, min(max1, max2) - max(min1, min2))

    def clean(self):
        date_time = self.data["date"]
        (start_hour, start_min, *_) = str.split(self.data["start_time"], ':')
        (end_hour, end_min, *_) = str.split(self.data["end_time"], ':')

        start_hour = int(start_hour)
        start_min = int(start_min)
        end_hour = int(end_hour)
        end_min = int(end_min)

        self.validatePeirod(start_hour, start_min, end_hour, end_min)

        for reservation in Reservation.objects.all():
            if reservation.room.id == self.data["room"]:
                if reservation.date == date_time:
                    this_start = start_hour * 100 + start_min
                    this_end = end_hour * 100 + end_min
                    other_start = int(reservation.start_time.split(':')[0]) * 100 + int(reservation.start_time.split(':')[1])
                    other_end = int(reservation.end_time.split(':')[0]) * 100 + int(reservation.end_time.split(':')[1])

                    if self.overlap(this_start, this_end, other_start, other_end) > 0:
                        raise ValidationError("Sala jest już zajęta w tym czasie")

        return self.cleaned_data

    def validatePeirod(self, start_hour, start_min, end_hour, end_min):
        if (end_hour * 60 + end_min) < (start_hour * 60 + start_min):
            period = (((24 - start_hour) * 60) + start_min) + ((end_hour * 60) + end_min)
        else:
            period = (end_hour - start_hour) * 60 + (end_min - start_min)

        if period < 15:
            raise ValidationError("Minimalny czas rezerwacji to 15 minut")

        if period > 8 * 60:
            raise ValidationError("Maksymalny czas rezerwacji to 8 godzin")
