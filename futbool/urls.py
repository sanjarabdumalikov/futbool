# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserRegistrationView, ObtainAuthToken,
    LandOwnerViewSet, FootballFieldViewSet, ReservationViewSet,
)

router = DefaultRouter()
router.register(r'land-owners', LandOwnerViewSet)
router.register(r'football-fields', FootballFieldViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('token/', ObtainAuthToken.as_view(), name='user-token'),
]

urlpatterns += router.urls
