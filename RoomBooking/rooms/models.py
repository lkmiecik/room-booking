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
    seats = models.IntegerField(default=0)
    equipment = models.CharField(max_length=300, null=True, blank=True)
    disability = models.BooleanField(default=True)
    floor = models.IntegerField(default=0)

    def __str__(self):
        return f"Sala o numerze {self.number}"

class User(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    email = models.CharField(max_length=200, null=True, blank=True)
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.email}"


class Reservation(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    #duration = models.IntegerField(default=15)
    day = models.DateField()
    starts = models.TimeField()
    ends = models.TimeField()
    who = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Rezerwacja w pokoju {self.room.number} przez użytkownika {self.who} "

    def clean(self):
        print('time', self.starts)
        all_reservations = Reservation.objects.distinct()
        for r in all_reservations:
            print(r.room.number, self.room.number)