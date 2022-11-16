from django.shortcuts import render
from rest_framework import generics

from main.models import Tarif, Date, Price, Contact
from main.serializers import TarifSerializer, DateSerializer, PriceSerializer, ContactSerializer


# Create your views here.
class TarifViewSet(generics.ListAPIView):
    queryset = Tarif.objects.all()
    serializer_class = TarifSerializer


class DateViewSet(generics.ListAPIView):
    queryset = Date.objects.all()
    serializer_class = DateSerializer


class PriceViewSet(generics.ListAPIView):
    serializer_class = PriceSerializer

    def get_queryset(self):
        queryset = Price.objects.all()
        tarif = self.request.query_params.get('tarif', None)
        date = self.request.query_params.get('date', None)
        if tarif:
            queryset = queryset.filter(tarif=tarif)
            if date:
                queryset = queryset.filter(date=date)
        elif date:
            queryset = queryset.filter(date=date)
            if tarif:
                queryset = queryset.filter(tarif=tarif)
        return queryset


class ContactViewSet(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
