from django.shortcuts import render
from rest_framework import generics

from payment.models import Booking
from payment.serializers import BookingSerializer


# Create your views here.
class BookingViewSet(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
