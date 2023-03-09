import uuid
from enum import Enum

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
    floor_number = models.IntegerField(null=False)

    def __str__(self):
        return f"Sala o numerze {self.number}"


class MetadataName(Enum):
    wheelchair_access = 'wheelchair_access'
    projector = 'projector'
    whiteboard = 'whiteboard'
    speakers = 'speakers'
    def display(self):
        translations = {
            MetadataName.wheelchair_access: 'Dostęp dla wózków',
            MetadataName.projector: 'Projektor',
            MetadataName.whiteboard: 'Tablica suchościeralna',
            MetadataName.speakers: 'Głośniki',
        }
        return translations.get(self, self.value)

class RoomMetadata(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(choices=[(e.value, e.name) for e in MetadataName], max_length=50)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Presenter(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"prezenter {self.name}"


class Booking(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=32)
    start = models.DateTimeField(null=False)
    end = models.DateTimeField(null=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    presenter = models.ForeignKey(Presenter, on_delete=models.CASCADE)

    def __str__(self):
        return f"Booking {self.name}"
