# views.py
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status

from .serializers import CustomTokenObtainPairSerializer, RegisterSerializer, UserSerializer


# Login view
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# Registration view
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User created successfully",
        }, status=status.HTTP_201_CREATED)


# Display available routes
class APIRootView(APIView):
    def get(self, request):
        return Response({
            "token": "/auth/token/",
            "token_refresh": "/auth/token/refresh/",
            "register": "/auth/register/",
        })
