# project_name/settings.py

INSTALLED_APPS = [
    ...,
    'rest_framework',
    'hotelapp',
]

# project_name/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('hotelapp.urls')),
]

# hotelapp/models.py
from django.db import models

class Hotels(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    availability = models.BooleanField(default=False)

class Reservation(models.Model):
    reservation_id = models.BigAutoField(primary_key=True)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()

class Guest(models.Model):
    guest_id = models.BigAutoField(primary_key=True)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=20)
    email = models.CharField(max_length=200)

# hotelapp/serializers.py
from rest_framework import serializers
from .models import Hotels, Reservation, Guest

class HotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'

# hotelapp/views.py
from rest_framework import viewsets
from .models import Hotels, Reservation, Guest
from .serializers import HotelsSerializer, ReservationSerializer, GuestSerializer

class HotelsViewSet(viewsets.ModelViewSet):
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

# hotelapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelsViewSet, ReservationViewSet, GuestViewSet

router = DefaultRouter()
router.register(r'hotels', HotelsViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'guests', GuestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# 终端运行以下命令以启用模型：
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
