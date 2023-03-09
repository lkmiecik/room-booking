from django.contrib import admin
from .models import Sala, Wynajem, RFID, Cena, Building

# Register your models here.
admin.site.register(Sala)
admin.site.register(Wynajem)
admin.site.register(RFID)
admin.site.register(Cena)
admin.site.register(Building)


