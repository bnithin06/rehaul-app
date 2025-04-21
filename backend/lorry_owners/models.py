from django.db import models
from django.conf import settings

class Lorry(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lorries')
    registration_number = models.CharField(max_length=20, unique=True)
    capacity_in_tons = models.FloatField()
    vehicle_type = models.CharField(max_length=50)
    manufacture_year = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.registration_number} ({self.owner.phone_number})"
