from django.db import models

from main.models import Date, Price, Tarif


# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    tarif = models.ForeignKey(Tarif, on_delete=models.CASCADE)
    flight_date = models.ForeignKey(Date, on_delete=models.CASCADE)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    number_of_passengers = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
