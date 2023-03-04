from django.forms import ModelForm, CharField
from django.core.exceptions import ValidationError
from .models import Building


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

