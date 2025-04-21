from rest_framework import serializers
from .models import LoadRequest

class LoadRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadRequest
        fields = '__all__'
