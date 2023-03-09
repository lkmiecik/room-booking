from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),


    path('rooms', views.rooms, name='rooms'),
    path('room/<str:pk>', views.room, name='room'),
    path('room/create-room/', views.createRoom, name='create-room'),
    path('room/update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('room/delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),

    path('buildings', views.buildings, name='buildings'),
    path('building/<str:pk>/', views.building, name="building"),
    path('create-building/', views.createBuilding, name='create-building'),
    path('update-building/<str:pk>/', views.updateBuilding, name="update-building"),
    path('delete-building/<str:pk>/', views.deleteBuilding, name="delete-building"),

    path('reservations', views.reservations, name='reservations'),
    # path('building/<str:pk>/', views.building, name="building"),
    # path('create-building/', views.createBuilding, name='create-building'),
    # path('update-building/<str:pk>/', views.updateBuilding, name="update-building"),
    path('delete-reservation/<str:pk>/', views.deleteReservation, name="delete-reservation"),


    path('sala/edit/<int:id>', views.home, name='edit_sala'),
    path('', include('django.contrib.auth.urls'))
]