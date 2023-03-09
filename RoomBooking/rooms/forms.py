from datetime import datetime

from django.forms import ModelForm, CharField, ModelChoiceField, DateTimeField, DateTimeInput, IntegerField, \
    ModelMultipleChoiceField, BooleanField
from django.core.exceptions import ValidationError
from .models import Building, Room, Booking, Presenter, MetadataName, RoomMetadata


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in MetadataName:
            init = RoomMetadata.objects.filter(room=self.instance.id, name=name.value).first()
            self.fields[name.value] = BooleanField(label=MetadataName(name.name).display(), required=False, initial=init)

    def save(self, commit=True):
        room = super().save(commit=False)

        if commit:
            room.save()

        RoomMetadata.objects.filter(room=room).delete()
        for name in MetadataName:
            if self.cleaned_data.get(name.value):
                RoomMetadata.objects.create(name=name.value, room=room)
        return room

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
        self.fields['room'].label_from_instance = lambda obj: f"{obj} ({obj.building})"

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start')
        end_time = cleaned_data.get('end')
        room = cleaned_data.get('room')
        booking_id = self.instance.id if self.instance else None

        if start_time and end_time and start_time >= end_time:
            raise ValidationError('Godzina zakończenia musi być późniejsza niż godzina rozpoczęcia.')

        if (end_time - start_time).seconds // 3600 > 8:
            raise ValidationError('Rezerwacja nie może trwać dłużej niż 8 godzin.')

        if Booking.objects.filter(room=room, start__lt=end_time, end__gt=start_time).exclude(id=booking_id):
            raise ValidationError('Wybrana sala jest już zarezerwowana w tym czasie.')

        return cleaned_data

    class Meta:
        model = Booking
        fields = ['name', 'room', 'start', 'end', 'presenter']
