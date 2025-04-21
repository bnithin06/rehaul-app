from rest_framework import generics, permissions
from .models import LoadRequest
from .serializers import LoadRequestSerializer

class LoadRequestListCreateView(generics.ListCreateAPIView):
    serializer_class = LoadRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return LoadRequest.objects.filter(posted_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)