from django.contrib import admin
from .models import DriverProfile

@admin.register(DriverProfile)
class DriverProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'license_number', 'driving_experience', 'vehicle_type', 'is_available')
    search_fields = ('user__phone_number', 'license_number', 'aadhar_number')
    list_filter = ('is_available', 'vehicle_type')