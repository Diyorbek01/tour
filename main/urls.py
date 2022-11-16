from django.urls import path

from main.views import TarifViewSet, DateViewSet, PriceViewSet, ContactViewSet

urlpatterns = [
    path('tarif/', TarifViewSet.as_view()),
    path('date/', DateViewSet.as_view()),
    path('price/', PriceViewSet.as_view()),
    path('contact/', ContactViewSet.as_view()),
]
