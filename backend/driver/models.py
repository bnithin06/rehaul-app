from django.db import models
from django.conf import settings

class DriverProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='driver_profile'
    )
    license_number = models.CharField(max_length=20, unique=True)
    license_expiry = models.DateField(null=True, blank=True)
    driving_experience = models.PositiveIntegerField(help_text="Experience in years")
    vehicle_type = models.CharField(max_length=50, help_text="E.g., Truck, Lorry, Container", blank=True, null=True)
    aadhar_number = models.CharField(max_length=12, unique=True)
    profile_picture = models.ImageField(upload_to='driver/profile_pics/', null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)  # To accept new load or not
    current_location = models.CharField(max_length=100, blank=True, null=True)  # GPS if you want later

    def __str__(self):
        return f"Driver: {self.user.phone_number}"
