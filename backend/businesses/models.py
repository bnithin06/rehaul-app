from django.db import models
from django.conf import settings

class LoadRequest(models.Model):
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='load_requests')
    source_location = models.CharField(max_length=100)
    destination_location = models.CharField(max_length=100)
    goods_type = models.CharField(max_length=100)
    quantity = models.FloatField(help_text="In tons or units")
    required_date = models.DateField()
    urgency = models.CharField(max_length=20, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    
    def __str__(self):
        return f"Load: {self.goods_type} from {self.source_location} to {self.destination_location}"