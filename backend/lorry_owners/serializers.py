from rest_framework import serializers
from .models import Lorry

class LorrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lorry
        fields = '__all__'