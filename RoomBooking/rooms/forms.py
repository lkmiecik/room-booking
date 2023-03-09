from django.forms import ModelForm, CharField, ModelChoiceField, TimeField, DateField, SelectDateWidget, DateInput
from django.core.exceptions import ValidationError
from .models import Building, Room, User, Reservation
import time, datetime


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
    #seats = CharField(label='Ilość miejsc w sali')

    class Meta:
        model = Room
        fields = '__all__'


class UserForm(ModelForm):
    email = CharField(label="E-mail")
    fname = CharField(label="Imię")
    lname = CharField(label="Nazwisko")

    class Meta:
        model = User
        fields = '__all__'


class ReservationForm(ModelForm):
    room = ModelChoiceField(label='Pokój', queryset=Room.objects.all())
    #duration = IntegerField(label="Czas trwania")
    day = DateField(label="Dzień", initial=time.time(), widget=SelectDateWidget(empty_label=("Wybierz rok", "Wybierz miesiąc", "Wybierz dzień")))
    starts = TimeField(label="Początek", widget=DateInput(attrs={'type': 'time'}))
    ends = TimeField(label="Koniec", widget=DateInput(attrs={'type': 'time'}))
    who = ModelChoiceField(label="Użytkownik", queryset=User.objects.all())

    class Meta:
        model = Reservation
        fields = '__all__'