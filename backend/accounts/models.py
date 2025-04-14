from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The phone number must be set")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone_number, password, **extra_fields)

class User(AbstractUser):
    ROLE_CHOICES = [
        ('driver', 'Driver'),
        ('lorry_owner', 'Lorry Owner'),
        ('business', 'Business Person'),
        ('admin', 'Admin'),
    ]

    phone_number = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='driver')

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']  # keep this because AbstractUser expects username field
    
    objects = UserManager()

    def __str__(self):
        return self.phone_number

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