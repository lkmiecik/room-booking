from django.contrib import admin

from .models import Building, Room, User, Reservation

# Register your models here.
admin.site.register(Building)
admin.site.register(Room)
admin.site.register(User)
admin.site.register(Reservation)
