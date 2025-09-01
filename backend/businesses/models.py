from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
print(User)

class Load(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    weight = models.FloatField()
    material_type = models.CharField(max_length=100)
    pickup_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.source} ➝ {self.destination}"
