import json
import uuid
from datetime import datetime, timedelta

import jwt
import stripe
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken

from core import settings
from reservation.models import Sala, Wynajem
from .serializers import SzukajSerializer, RegistrationSerializer, SzukajSerializer, SalaSerializer, WynajmijSerializer


class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "message": "Użytkownik utworzony prawidłowo",
                "User": {
                    "first_name": serializer.data['first_name'],
                    "last_name": serializer.data['last_name'],
                    "email": serializer.data['email'],
                    "username": serializer.data['username'],
                }}, status=status.HTTP_201_CREATED)

        print(serializer.errors)

        return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# class dostepneSale(viewsets.ModelViewSet):
#     # permission_classes = (IsAuthenticated, )
#     serializer_class = SzukajSerializer
#
#
#
#     print(queryset)
#

class dostepneSale(generics.GenericAPIView):
    serializer_class = SzukajSerializer

    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = SzukajSerializer(data=request.data)
        if serializer.is_valid():
            pass

        data = serializer.data

        if len(data['wynajem_od'] or "") < 3:
            return Response({"error": "Data startu wynajmu jest pusta"})

        if len(data['wynajem_do'] or "") < 3:
            return Response({"error": "Data końca wynajmu jest pusta"})

        rzutnik = data['rzutnik'] or False
        audio = data['audio'] or False
        tablica = data['tablica'] or False
        wifi = data['wifi'] or False
        klimatyzacja = data['klimatyzacja'] or False
        catering = data['catering'] or False
        czy_dostepna_dla_osob_z_niepelnosprawnoscia = data['czy_dostepna_dla_osob_z_niepelnosprawnoscia'] or False

        # sala według wymagań
        queryset = Sala.objects.filter(
            Q(rzutnik=rzutnik),
            Q(audio=audio),
            Q(tablica=tablica),
            Q(wifi=wifi),
            Q(klimatyzacja=klimatyzacja),
            Q(catering=catering),
            Q(max_osob__gte=data['ilosc_osob']),
            Q(czy_dostepna_dla_osob_z_niepelnosprawnoscia=czy_dostepna_dla_osob_z_niepelnosprawnoscia)
        )

        # sprawdzanie czy sala zgodna z wymaganiami posiada wynajem
        # jeżeli posiada wynajem to wtedy pokaż inne

        sale = []  # dostępne sale według kryteirów

        for q in queryset:
            query = Wynajem.objects.filter(
                Q(wynajem_od=data['wynajem_od']),
                Q(wynajem_do=data['wynajem_do']),
                Q(sala__id=q.id)
            )

            if len(query) <= 0:
                sale.append(q)

        # sale dostepne
        dostepne_sale = []

        if len(sale) <= 0:
            sale = "Brak"
        else:
            for i, sala in enumerate(sale):
                if i > 2:  # limit do wyświetlania max 3 requestów
                    break
                dostepne_sale.append({
                    "id": sala.id,
                    "nazwa_sali": sala.nazwa_sali,
                    "max_ilosc_osob": sala.max_osob,
                    "rzutnik": sala.rzutnik,
                    "tablica": sala.tablica,
                    "audio": sala.audio,
                    "catering": sala.catering,
                    "wifi": sala.wifi,
                    "klimatyzacja": sala.klimatyzacja,
                    "czy_dostepna_dla_osob_z_niepelnosprawnoscia": sala.czy_dostepna_dla_osob_z_niepelnosprawnoscia,
                    "area": sala.area,
                    "pietro": sala.pietro,
                    "building": {
                        "id": sala.building.id,
                        "number": sala.building.number,
                        "street": sala.building.street,
                        "town": sala.building.town,
                        "zip_code": sala.building.zip_code,
                    },
                    "cennik": {
                        "id": sala.cennik.id,
                        "rzutnik": sala.cennik.rzutnik_cena,
                        "tablica": sala.cennik.tablica,
                        "audio": sala.cennik.audio,
                        "catering": sala.cennik.catering,
                        "wifi": sala.cennik.wifi,
                        "klimatyzacja": sala.cennik.klimatyzacja,
                        "currency": sala.cennik.currency
                    },
                    "mozliwosc_rezerwacji_od": sala.mozliwosc_rezerwacji_od,
                    "mozliwosc_rezerwacji_do": sala.mozliwosc_rezerwacji_do
                })

        return Response({"available": dostepne_sale})

class WynajetePrzezUseraAPI(generics.GenericAPIView):
    permission_classes = (IsAuthenticated, )
    # serializer_class = WynajetePrzezUseraSerializer

    def get(self, request):
        # serializer = WynajetePrzezUseraSerializer(data=request.data)

        # if serializer.is_valid():
        #     data = serializer.data

        user = self.request.user

        print(user)

        querydict = Wynajem.objects.filter(user=user)
        print(querydict)

        arr = []

        for q in querydict:
            arr.append({
                "wynajem_od": q.wynajem_od,
                "wynajem_do": q.wynajem_do,
                "status_transakcji": q.status_transakcji,
                "sala": {
                    "id": q.sala.id,
                    "nazwa_sali": q.sala.nazwa_sali,
                    "max_ilosc_osob": q.sala.max_osob,
                    "rzutnik": q.sala.rzutnik,
                    "tablica": q.sala.tablica,
                    "audio": q.sala.audio,
                    "catering": q.sala.catering,
                    "wifi": q.sala.wifi,
                    "klimatyzacja": q.sala.klimatyzacja,
                    "czy_dostepna_dla_osob_z_niepelnosprawnoscia": q.sala.czy_dostepna_dla_osob_z_niepelnosprawnoscia,
                    "area": q.sala.area,
                    "pietro": q.sala.pietro,
                    "building": {
                        "id": q.sala.building.id,
                        "number": q.sala.building.number,
                        "street": q.sala.building.street,
                        "town": q.sala.building.town,
                        "zip_code": q.sala.building.zip_code,
                    },
                    "cennik": {
                        "id": q.sala.cennik.id,
                        "rzutnik": q.sala.cennik.rzutnik_cena,
                        "tablica": q.sala.cennik.tablica,
                        "audio": q.sala.cennik.audio,
                        "catering": q.sala.cennik.catering,
                        "wifi": q.sala.cennik.wifi,
                        "klimatyzacja": q.sala.cennik.klimatyzacja,
                        "currency": q.sala.cennik.currency
                    },
                    "mozliwosc_rezerwacji_od": q.sala.mozliwosc_rezerwacji_od,
                    "mozliwosc_rezerwacji_do": q.sala.mozliwosc_rezerwacji_do
                }
            })

        return Response({
            "rented": arr
        })

    # return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class salaInfo(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        sala = get_object_or_404(Sala, id=id)
        serializer = SalaSerializer(sala, many=False)
        return Response(serializer.data)


class Wynajmij(generics.GenericAPIView):
    serializer_class = WynajmijSerializer

    def post(self, request):
        self.permission_classes = (IsAuthenticated,)

        try:
            serializer = self.get_serializer(data=request.data, context={
                "user_id": AccessToken(str(self.request.auth))['user_id']
            })
        except Exception:
            return Response({'message': 'Błąd tokenu'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            wynajem = serializer.save()

            suma_za_sale = 0.0

            if wynajem.sala.tablica:
                suma_za_sale += wynajem.sala.cennik.tablica

            if wynajem.sala.rzutnik:
                suma_za_sale += wynajem.sala.cennik.rzutnik_cena

            if wynajem.sala.audio:
                suma_za_sale += wynajem.sala.cennik.audio

            if wynajem.sala.catering:
                suma_za_sale += (wynajem.sala.cennik.catering * wynajem.sala.max_osob)

            if wynajem.sala.wifi:
                suma_za_sale += wynajem.sala.cennik.wifi

            if wynajem.sala.klimatyzacja:
                suma_za_sale += wynajem.sala.cennik.klimatyzacja

            suma_za_sale += (wynajem.sala.max_osob * wynajem.sala.cennik.cena_za_osobe)

            stripe.api_key = settings.STRIPE_API_KEY
            domain = 'http://192.168.1.188:8000/api/wynajmij/'
            checkout_session = stripe.checkout.Session.create(
                line_items=[{
                    'price_data': {
                        'currency': str(wynajem.sala.cennik.currency),
                        'product_data': {
                            'name': str(wynajem.sala.nazwa_sali),
                        },
                        'unit_amount': int(suma_za_sale * 100),
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=domain + f"?success=true&token={str(self.request.auth)}&wynajem_id={str(wynajem.id)}",
                cancel_url=domain + "?canceled=true"
            )

            Wynajem.objects.filter(id=wynajem.id).update(id_stripe=checkout_session.id)

            return Response({
                "message": "success",
                "checkout_url": checkout_session.url
            },
                status=status.HTTP_200_OK)

        return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        success = request.query_params.get('success')
        jwt_token = request.query_params.get('token')
        wynajem_id = request.query_params.get('wynajem_id')

        if success:
            try:
                user_id = AccessToken(str(jwt_token))['user_id']
            except Exception as E:
                return HttpResponse(f"Niepoprawny token. Prosimy o kontakt z {settings.HELP_EMAIL}")
            wynajem = Wynajem.objects.filter(id=wynajem_id).update(status_transakcji=True)

            return HttpResponse("Płatność zakończona! Możesz zamknąć tę kartę <script>window.close()</script>")
        else:
            return Response({"message": "Nieudana płatność."}, status=status.HTTP_400_BAD_REQUEST)
