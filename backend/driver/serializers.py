from rest_framework import serializers
from .models import DriverProfile

class DriverProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverProfile
        fields = '__all__'
        read_only_fields = ['user']