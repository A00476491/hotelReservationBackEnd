from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Hotels, Reservation, Guest
from .serializers import HotelsSerializer, ReservationSerializer, GuestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Hotels, Reservation, Guest
from django.shortcuts import get_object_or_404
import random, string

@api_view(['GET'])
def get_all_hotels(request):
    try:
        hotels = Hotels.objects.all()
        serializer = HotelsSerializer(hotels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_reservation(request):
    print(request.data)
    try:
        hotel_name = request.data.get("hotel_name")
        checkin = request.data.get("checkin")
        checkout = request.data.get("checkout")
        guests_list = request.data.get("guests_list")

        hotel = get_object_or_404(Hotels, name=hotel_name)

        confirmation_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

        reservation = Reservation.objects.create(
            hotel=hotel,
            checkin=checkin,
            checkout=checkout,
            confirmation_number=confirmation_number
        )

        for guest in guests_list:
            Guest.objects.create(
                reservation=reservation,
                name=guest["guest_name"],
                gender=guest["gender"]
            )

        return Response({
            "confirmation_number": confirmation_number,
            "reservation_id": reservation.reservation_id
        }, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_reservations(request):
    try:
        reserveations = Reservation.objects.all()
        serializer = ReservationSerializer(reserveations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_guests(request):
    try:
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)