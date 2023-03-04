from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('buildings', views.buildings, name='buildings'),
    path('building/<str:pk>/', views.building, name="building"),
    path('create-building/', views.createBuilding, name='create-building'),
    path('update-building/<str:pk>/', views.updateBuilding, name="update-building"),
    path('delete-building/<str:pk>/', views.deleteBuilding, name="delete-building"),
]

