from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import create_reservation, get_all_hotels, get_all_reservations, get_all_guests

urlpatterns = [
    path('create_reservation/', create_reservation),
    path('hotels/', get_all_hotels),
    path('reservations/', get_all_reservations),
    path('guests/', get_all_guests),
]