from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class APIRootView(APIView):
    def get(self, request):
        return Response({
            "token": "/auth/token/",
            "token_refresh": "/auth/token/refresh/",
        })