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

    path('book-room', views.bookRoom, name="book-room"),
    path('booked-rooms', views.reservations, name="booked-rooms"),
]

