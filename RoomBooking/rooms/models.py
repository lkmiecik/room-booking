from django.db import models


class Building(models.Model):
    number = models.CharField(max_length=32)


class Room(models.Model):
    number = models.CharField(max_length=32)
    area = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
