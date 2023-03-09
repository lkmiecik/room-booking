from django.forms import ModelForm, CharField, ModelChoiceField, BooleanField
from django.core.exceptions import ValidationError
from .models import Building, Room, Reservation


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
    capacity = CharField(label="Pojemność")
    eqiupment = CharField(label="Wyposażenie")
    disabledFriendly = CharField(label="Dostęp dla osób z niepełnosprawnością")
    building = ModelChoiceField(label='Budynek', queryset=Building.objects.all())
    floor = CharField(label="Piętro")

    class Meta:
        model = Room
        fields = '__all__'


class ReservationForm(ModelForm):
    rezerwujacy = CharField(label='Rezerwujacy')
    data = CharField(label='Data')
    building = ModelChoiceField(label='Pokoj', queryset=Room.objects.all())

    class Meta:
        model = Reservation
        fields = '__all__'
