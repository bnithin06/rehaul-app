from rest_framework import viewsets
from .serializers import LoadSerializer
from .models import Load
class LoadViewSet(viewsets.ModelViewSet):
    serializer_class = LoadSerializer
    queryset = Load.objects.all()


