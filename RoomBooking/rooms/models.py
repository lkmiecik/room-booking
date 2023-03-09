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
    area = models.CharField(null=True, blank=True, max_length=3)
    capacity = models.DecimalField(null=True, blank=True, decimal_places=0, max_digits=4)
    eqiupment = models.CharField(null=True, blank=True, max_length=200)
    disabledFriendly = models.BooleanField(null=False)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    floor = models.CharField(max_length=2)


    def __str__(self):
        return f"Sala o numerze {self.number}"

class Reservation(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    rezerwujacy = models.CharField(max_length=64, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateTimeField()
    duration = models.TimeField()

    def __str__(self):
        return f"Rezerwacja dla {self.rezerwujacy}"
