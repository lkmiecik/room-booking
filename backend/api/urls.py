from rest_framework_simplejwt import views as jwt_views
from django.urls import path
from . import views
from .views import RegistrationAPIView

urlpatterns = [
    # lista sal
    # path('sale/', views., name="lista_sal"),
    path('sale/<int:id>/', views.salaInfo.as_view()),
    path('szukaj/', views.dostepneSale.as_view()),
    # path('', views.Kongo.as_view()),

    path('wynajmij/', views.Wynajmij.as_view()),
    path('rented/', views.WynajetePrzezUseraAPI.as_view()),

    path('auth/register/', RegistrationAPIView.as_view(), name="register"),
    path('auth/login/', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('token/refresh-token/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
