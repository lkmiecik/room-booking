from datetime import datetime

from django.forms import ModelForm, CharField, ModelChoiceField, DateTimeField, DateTimeInput, IntegerField
from django.core.exceptions import ValidationError
from .models import Building, Room, Booking, Presenter


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
    floor_number = IntegerField(label='Pientro')

    class Meta:
        model = Room
        fields = '__all__'


class PresenterForm(ModelForm):
    name = CharField(label='Imię i nazwisko')

    class Meta:
        model = Presenter
        fields = '__all__'


def time_step_validator(value):
    error_message = f"Rezerwacja może być dokonywana z gradacją 15 minutową"
    if value.minute % 15 != 0:
        raise ValidationError(error_message)


class BookingForm(ModelForm):
    name = CharField(label='Nazwa rezerwacji')
    room = ModelChoiceField(label='Sala', queryset=Room.objects.all())
    start = DateTimeField(label='Data i godzina rozpoczęcia', widget=DateTimeInput(attrs={'type': 'datetime-local'}),
                          validators=[time_step_validator])
    end = DateTimeField(label='Data i godzina zakończenia', widget=DateTimeInput(attrs={'type': 'datetime-local'}),
                        validators=[time_step_validator])
    presenter = ModelChoiceField(label='Rezerwujący', queryset=Presenter.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start'].widget.attrs['step'] = 900
        self.fields['end'].widget.attrs['step'] = 900
        self.fields['room'].room_label = self.room_label

    def room_label(self, obj: Room):
        return f"Sala o numerze {obj.number} w budynku {obj.building.number}"
    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start')
        end_time = cleaned_data.get('end')
        room = cleaned_data.get('room')

        if start_time and end_time and start_time >= end_time:
            raise ValidationError('Godzina zakończenia musi być późniejsza niż godzina rozpoczęcia.')

        if (end_time - start_time).seconds // 3600 > 8:
            raise ValidationError('Rezerwacja nie może trwać dłużej niż 8 godzin.')

        if Booking.objects.filter(room=room, start__lt=end_time, end__gt=start_time):
            raise ValidationError('Wybrana sala jest już zarezerwowana w tym czasie.')

        return cleaned_data

    class Meta:
        model = Booking
        fields = ['name', 'room', 'start', 'end', 'presenter']
