from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    DRIVER = 'driver'
    LORRY_OWNER = 'lorry_owner'
    BUSINESS = 'business'
    ADMIN = 'admin'

    ROLE_CHOICES = [
        (DRIVER, _('Driver')),
        (LORRY_OWNER, _('Lorry Owner')),
        (BUSINESS, _('Business Person')),
        (ADMIN, _('Admin')),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=DRIVER,
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    
    def __str__(self):
        return self.username

class DriverProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='driver_profile')
    license_number = models.CharField(max_length=20)
    driving_experience = models.IntegerField()
    vehicle_type = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return f"Driver: {self.user.username}"

class LorryOwnerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='lorry_owner_profile')
    company_name = models.CharField(max_length=100)
    number_of_vehicles = models.IntegerField()
    business_registration_number = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Lorry Owner: {self.company_name}"

class BusinessProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='business_profile')
    business_name = models.CharField(max_length=100)
    business_type = models.CharField(max_length=50)
    address = models.TextField()
    
    def __str__(self):
        return f"Business: {self.business_name}"