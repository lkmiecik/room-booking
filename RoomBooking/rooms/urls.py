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

    path('presenters', views.presenters, name='presenters'),
    path('presenter/<str:pk>/', views.presenter, name="presenter"),
    path('create-presenter/', views.createPresenter, name='create-presenter'),
    path('update-presenter/<str:pk>/', views.updatePresenter, name="update-presenter"),
    path('delete-presenter/<str:pk>/', views.deletePresenter, name="delete-presenter"),

    path('bookings', views.bookings, name='bookings'),
    path('booking/<str:pk>/', views.booking, name="booking"),
    path('create-booking/', views.createBooking, name='create-booking'),
    path('update-booking/<str:pk>/', views.updateBooking, name="update-booking"),
    path('delete-booking/<str:pk>/', views.deleteBooking, name="delete-booking"),

    path('book-room/<str:pk>/', views.bookRoom, name='book-room'),

]

