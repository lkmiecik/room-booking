from django.forms import ModelForm, CharField, ModelChoiceField, IntegerField, BooleanField, DateTimeField, TimeField
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
    building = ModelChoiceField(label='Budynek', queryset=Building.objects.all())
    volume = IntegerField(label='Pojemnosc (ludzie)')
    floor = IntegerField(label='Pietro')
    handicapped = BooleanField(label='Dostęp dla osób z niepełnosprawnością')
    equipment = CharField(label='Wyposazenie')

    class Meta:
        model = Room
        fields = '__all__'


class ReservationForm(ModelForm):
    start = DateTimeField(label='Rozpoczecie')
    time = TimeField(label='Dlugosc')

    class Meta:
        model = Reservation
        fields = '__all__'

