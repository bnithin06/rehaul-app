from django.contrib import admin
from .models import Lorry

@admin.register(Lorry)
class LorryAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'owner', 'capacity_in_tons', 'vehicle_type', 'manufacture_year')
    search_fields = ('registration_number', 'owner__phone_number')
    list_filter = ('vehicle_type',)