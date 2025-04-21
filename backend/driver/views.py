from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from .models import DriverProfile
from .serializers import DriverProfileSerializer

class DriverProfileView(RetrieveUpdateAPIView):
    serializer_class = DriverProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            return self.request.user.driver_profile
        except DriverProfile.DoesNotExist:
            raise NotFound("Driver profile not found.")
