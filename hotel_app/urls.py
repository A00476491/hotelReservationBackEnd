from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelsViewSet, ReservationViewSet, GuestViewSet, HotelsCreateView

router = DefaultRouter()
router.register(r'hotels', HotelsViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'guests', GuestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('hotelaaa/', HotelsCreateView.as_view(), name='hotel2'),
]