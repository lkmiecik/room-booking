import uuid

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Cena(models.Model):
    nazwa_cennika = models.CharField(max_length=255, blank=False, default="Cennik")
    rzutnik_cena = models.FloatField(blank=False, default=100)
    tablica = models.FloatField(blank=False, default=20)
    audio = models.FloatField(blank=False, default=250)
    catering = models.FloatField(blank=False, help_text="Za osobę", default=14.97)
    wifi = models.FloatField(blank=False, default=50)
    klimatyzacja = models.FloatField(blank=False, default=300)
    cena_za_osobe = models.FloatField(blank=False, default=20)
    currency = models.CharField(max_length=3, choices=(
        ("pln", "pln"),
        ("usd", "usd"),
        ("eur", "eur")
    ), default='pln')

    def __str__(self):
        return f"{self.nazwa_cennika}"


class Building(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False),
    number = models.CharField(max_length=32)
    street = models.CharField(max_length=128, default="")
    town = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return f"Budynek o numerze {self.number}"


class Sala(models.Model):
    max_osob = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(500)],
                                           help_text="Ile osób zmieści się w sali?")
    tablica = models.BooleanField(default=False, help_text="Czy tablica do pisania ma być dostępna?")
    rzutnik = models.BooleanField(default=True, help_text="Czy rzutnik jest dostępny w tej sali?")
    audio = models.BooleanField(default=False,
                                help_text="Czy system nagłośnienia ma być dostępny do wyboru w tej sali?")
    catering = models.BooleanField(default=False, help_text="Czy istnieje możliwość zamówienia cateringu?")
    wifi = models.BooleanField(default=False, help_text="Czy WIFI ma być dostępny przy wborze sali?")
    klimatyzacja = models.BooleanField(default=False, help_text="Czy klimatyzacja jest dostępna?")
    czy_dostepna_dla_osob_z_niepelnosprawnoscia = models.BooleanField(default=False, help_text="Czy sala jest przystosowana dla osób z niepełnosprawnościami?")
    nazwa_sali = models.CharField(max_length=20, unique=True)
    cennik = models.ForeignKey(Cena, on_delete=models.CASCADE)
    pietro = models.IntegerField(default=0)
    mozliwosc_rezerwacji_od = models.TimeField()
    mozliwosc_rezerwacji_do = models.TimeField()
    area = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=10)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nazwa_sali}"


class Wynajem(models.Model):
    wynajem_od = models.DateTimeField()
    wynajem_do = models.DateTimeField()
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    status_transakcji = models.BooleanField(default=False)
    id_stripe = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Id użytkownika: {self.user.id} | {self.sala.nazwa_sali} | Rezerwacja od: {self.wynajem_od} do {self.wynajem_do}"


class RFID(models.Model):
    rfid = models.CharField(max_length=255)
    sala = models.OneToOneField(Sala, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sala.nazwa_sali}"
