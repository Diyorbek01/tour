from django.urls import path

from payment.views import BookingViewSet

urlpatterns = [
    path('booking/', BookingViewSet.as_view())
]
