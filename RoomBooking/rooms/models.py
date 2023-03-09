import uuid

from django.db import models


class Building(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    number = models.CharField(max_length=32)
    street = models.CharField(max_length=128, default="")
    town = models.CharField(max_length=64, null=True, blank=True)
    zip_code = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return f"Budynek o numerze {self.number}"


class Room(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    number = models.CharField(max_length=32)
    area = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=10)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    floor = models.IntegerField(null=True, blank=False, default=0)
    capacity = models.IntegerField(null=True, blank=False, default=0)
    equipment = models.TextField(null=True, blank=True, default="")
    accessibility = models.BooleanField(default=False)

    def __str__(self):
        return f"Sala o numerze {self.number}"


class ReservingPerson(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Reservation(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    reserving_person = models.ForeignKey(ReservingPerson, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"Rezerwacja {self.room} od {self.start_time} do {self.end_time} przez {self.reserving_person}"
