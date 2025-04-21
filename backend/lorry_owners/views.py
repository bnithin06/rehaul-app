from rest_framework import generics, permissions
from .models import Lorry
from .serializers import LorrySerializer

class LorryListCreateView(generics.ListCreateAPIView):
    serializer_class = LorrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Lorry.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)