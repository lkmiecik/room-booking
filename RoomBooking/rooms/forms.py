from django.forms import ModelForm, CharField, ModelChoiceField, BooleanField, TimeField, DateTimeField
from django.core.exceptions import ValidationError
from .models import Building, Room, Reservation
from datetime import datetime


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

def res_validator(value):
    error_message = "Niepoprawna data"

    if value.hour > 8:
        raise ValidationError(error_message)

    if value.hour < 1 and value.minute < 15:
        raise ValidationError(error_message)


def date_validator(value):
    error_message = "Niepoprawna data"

    if value.minute == 15 or value.minute == 30 or value.minute == 45 or value.minute == 0:
        return True
    else:
        print(value.minute)
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
    capacity = CharField(label="Pojemność")
    eqiupment = CharField(label="Wyposażenie")
    disabledFriendly = BooleanField(label="Dostęp dla osób z niepełnosprawnością", required=False)
    building = ModelChoiceField(label='Budynek', queryset=Building.objects.all())
    floor = CharField(label="Piętro")

    class Meta:
        model = Room
        fields = '__all__'


class ReservationForm(ModelForm):
    rezerwujacy = CharField(label='Rezerwujacy')
    room = ModelChoiceField(label='Pokoj', queryset=Room.objects.all())
    date = DateTimeField(label='Data', validators=[date_validator])
    duration = TimeField(label='Czas trwania', validators=[res_validator])

    class Meta:
        model = Reservation
        fields = '__all__'
