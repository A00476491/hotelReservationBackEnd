from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Hotels, Reservation, Guest
from .serializers import HotelsSerializer, ReservationSerializer, GuestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class HotelsViewSet(viewsets.ModelViewSet):
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

@method_decorator(csrf_exempt, name='dispatch')
class HotelsCreateView(APIView):
    def get(self, request):
        hotels = Hotels.objects.all()
        serializer = HotelsSerializer(hotels, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HotelsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)