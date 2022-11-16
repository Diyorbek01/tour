import admin_thumbnails

from django.contrib import admin
from main.models import Tarif, Price, Date, Contact, Album

# Register your models here.
admin.site.register(Tarif)
admin.site.register(Date)


class PriceAdmin(admin.ModelAdmin):
    list_display = ['tarif', 'date', 'amount']
    list_filter = ['tarif', 'date', 'created_at']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'text', 'created_at']
    list_filter = ['created_at']


@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image_thumbnail']
    list_filter = ['created_at']


admin.site.register(Price, PriceAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Album, ImagesAdmin)
