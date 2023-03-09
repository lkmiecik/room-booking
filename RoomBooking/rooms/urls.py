from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('room/<str:pk>', views.room, name='room'),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('buildings', views.buildings, name='buildings'),
    path('building/<str:pk>/', views.building, name="building"),
    path('create-building/', views.createBuilding, name='create-building'),
    path('update-building/<str:pk>/', views.updateBuilding, name="update-building"),
    path('delete-building/<str:pk>/', views.deleteBuilding, name="delete-building"),
    path('reserving-persons', views.reservingPersons, name='reserving-persons'),
    path('reserving-person/<str:pk>/', views.reservingPerson, name="reserving-person"),
    path('create-reserving-person/', views.createReservingPerson, name='create-reserving-person'),
    path('delete-reserving-person/<str:pk>/', views.deleteReservingPerson, name="delete-reserving-person"),
]
