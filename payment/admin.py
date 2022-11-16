from django.contrib import admin

from payment.models import Booking


# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'tarif', 'flight_date', 'price', 'number_of_passengers']
    list_filter = ['tarif', 'flight_date', 'price', 'created_at']


admin.site.register(Booking, BookingAdmin)
