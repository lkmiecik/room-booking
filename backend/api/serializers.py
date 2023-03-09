from datetime import datetime, timedelta

import django.contrib.auth.password_validation as validators
from django.contrib.auth.models import User
from django.core import exceptions
from django.db.models import Q
from django.shortcuts import get_object_or_404
from phonenumber_field.formfields import PhoneNumberField
from django.utils import timezone

now = timezone.now()
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from reservation.models import Sala, Wynajem, Cena


class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = "__all__"


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        password = args.get('password', None)

        user = User(**args)

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Taki adres email jest już używany"})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"email": "Taka nazwa użytkownika jest już używana"})

        try:
            validators.validate_password(password=password, user=user)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})

        return super().validate(args)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


# class SzukajSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sala
#         fields = '__all__'
#         extra_kwargs = {
#             'tablica': {'default': False},
#             'rzutnik': {'default': True},
#             'audio': {'default': False},
#             'catering': {'default': False},
#             'wifi': {'default': False},
#             'klimatyzacja': {'default': False}
#         }
#         # Specify the default value for BooleanFields as Python booleans
#         boolean_fields = ['tablica', 'rzutnik', 'audio', 'catering', 'wifi', 'klimatyzacja']
#         for field_name in boolean_fields:
#             if field_name in extra_kwargs:
#                 extra_kwargs[field_name]['default'] = bool(extra_kwargs[field_name]['default'])
#
#     def to_internal_value(self, data):
#         # Deserialize boolean fields from string to Python bool
#         for field_name in self.Meta.boolean_fields:
#             if field_name in data:
#                 data[field_name] = bool(data[field_name])
#         return super().to_internal_value(data)

#
class SzukajSerializer(serializers.ModelSerializer):
    rzutnik = serializers.BooleanField(required=True)
    tablica = serializers.BooleanField(default=False)
    audio = serializers.BooleanField(default=False)
    catering = serializers.BooleanField(default=False)
    wifi = serializers.BooleanField(default=False)
    klimatyzacja = serializers.BooleanField(default=False)
    ilosc_osob = serializers.IntegerField(min_value=1, max_value=500, required=True)
    czy_dostepna_dla_osob_z_niepelnosprawnoscia = serializers.BooleanField(default=False)

    class Meta:
        model = Wynajem
        fields = (
            'wynajem_od', 'wynajem_do', 'rzutnik', 'audio', 'tablica', 'wifi', 'klimatyzacja', 'catering',
            'czy_dostepna_dla_osob_z_niepelnosprawnoscia', 'ilosc_osob')

    def validate(self, attrs):
        wynajem_od = attrs.get('wynajem_od', None)
        wynajem_do = attrs.get('wynajem_do', None)
        ilosc_osob = attrs.get('ilosc_osob', None)
        rzutnik = attrs.get('rzutnik', None)
        audio = attrs.get('audio', None)
        tablica = attrs.get('tablica', None)
        wifi = attrs.get('wifi', None)
        klimatyzacja = attrs.get('klimatyzacja', None)
        catering = attrs.get('catering', None)
        czy_dostepna_dla_osob_z_niepelnosprawnoscia = attrs.get('czy_dostepna_dla_osob_z_niepelnosprawnoscia', None)

        return super().validate(attrs)


# class WynajetePrzezUseraSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Wynajem
#         fields = (
#             'wynajem_od', 'wynajem_do', 'rzutnik', 'audio', 'tablica', 'wifi', 'klimatyzacja', 'catering',
#             'czy_dostepna_dla_osob_z_niepelnosprawnoscia', 'ilosc_osob')
#
#     def validate(self, args):
#         start_time = args.get('wynajem_od', None)
#         end_time = args.get('wynajem_do', None)
#         sala = args.get('sala', None)
#
#         if start_time.time() < sala.mozliwosc_rezerwacji_od or end_time.time() > sala.mozliwosc_rezerwacji_do:
#             raise serializers.ValidationError(
#                 {"rezerwacja": "Rezerwacja nie mieści się w godzinach możliwości rezerwacji sali"})
#
#         delta = end_time - start_time
#         if delta < timedelta(minutes=15):
#             raise serializers.ValidationError({"rezerwacja": "Minimalny czas rezerwacji to 15 minut"})
#
#         if delta > timedelta(hours=8):
#             raise serializers.ValidationError({"rezerwacja": "Maksymalny czas trwania rezerwacji to 8 godzin"})
#
#         if start_time.minute % 15 != 0:
#             raise serializers.ValidationError({
#                 "rezerwacja": "Godzina rozpoczęcia rezerwacji powinna być zgodna z 15-minutową gradacją. Np.: 12:15, 12:30"})
#
#         if delta.seconds % 900 != 0:
#             raise serializers.ValidationError(
#                 {"rezerwacja": "Czas trwania rezerwacji powinien być zgodny z 15-minutową gradacją"})
#
#         if timezone.now() > start_time:
#             raise serializers.ValidationError({"rezerwacja": "Nie można zarezerwować sali w przeszłości"})
#
#         if Wynajem.objects.filter(sala=sala, wynajem_od__lte=start_time, wynajem_do__gte=end_time).exists():
#             raise serializers.ValidationError({"rezerwacja": "Taka sala jest już zarezerwowana"})
#
#         return super().validate(args)
#

class WynajmijSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wynajem
        fields = ("wynajem_od", "wynajem_do", 'sala')

    def validate(self, args):
        start_time = args.get('wynajem_od', None)
        end_time = args.get('wynajem_do', None)
        sala = args.get('sala', None)

        if start_time.time() < sala.mozliwosc_rezerwacji_od or end_time.time() > sala.mozliwosc_rezerwacji_do:
            raise serializers.ValidationError(
                {"rezerwacja": "Rezerwacja nie mieści się w godzinach możliwości rezerwacji sali"})

        delta = end_time - start_time
        if delta < timedelta(minutes=15):
            raise serializers.ValidationError({"rezerwacja": "Minimalny czas rezerwacji to 15 minut"})

        if delta > timedelta(hours=8):
            raise serializers.ValidationError({"rezerwacja": "Maksymalny czas trwania rezerwacji to 8 godzin"})

        if start_time.minute % 15 != 0:
            raise serializers.ValidationError({"rezerwacja": "Godzina rozpoczęcia rezerwacji powinna być zgodna z 15-minutową gradacją. Np.: 12:15, 12:30"})

        if delta.seconds % 900 != 0:
            raise serializers.ValidationError({"rezerwacja": "Czas trwania rezerwacji powinien być zgodny z 15-minutową gradacją"})

        if timezone.now() > start_time:
            raise serializers.ValidationError({"rezerwacja": "Nie można zarezerwować sali w przeszłości"})

        if Wynajem.objects.filter(sala=sala, wynajem_od__lte=start_time, wynajem_do__gte=end_time).exists():
            raise serializers.ValidationError({"rezerwacja": "Taka sala jest już zarezerwowana"})

        return super().validate(args)

    def create(self, validated_data):
        user_id = self.context['user_id']
        return Wynajem.objects.create(**validated_data, user_id=user_id)
