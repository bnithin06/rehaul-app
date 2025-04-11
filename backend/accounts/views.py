from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from .serializers import (
    CustomTokenObtainPairSerializer, DriverRegistrationSerializer,
    LorryOwnerRegistrationSerializer, BusinessRegistrationSerializer,
    AdminRegistrationSerializer, UserSerializer
)
from .permissions import IsDriver, IsLorryOwner, IsBusiness, IsAdmin
from .models import DriverProfile, LorryOwnerProfile, BusinessProfile

User = get_user_model()

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class DriverRegistrationView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        serializer = DriverRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = CustomTokenObtainPairSerializer.get_token(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LorryOwnerRegistrationView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        serializer = LorryOwnerRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = CustomTokenObtainPairSerializer.get_token(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BusinessRegistrationView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        serializer = BusinessRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = CustomTokenObtainPairSerializer.get_token(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminRegistrationView(APIView):
    permission_classes = (IsAdmin,)  # Only admins can create other admins
    
    def post(self, request):
        serializer = AdminRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        
        # Add profile data based on user role
        data = serializer.data
        if user.role == User.DRIVER:
            try:
                profile = user.driver_profile
                data['profile'] = DriverProfileSerializer(profile).data
            except DriverProfile.DoesNotExist:
                pass
        elif user.role == User.LORRY_OWNER:
            try:
                profile = user.lorry_owner_profile
                data['profile'] = LorryOwnerProfileSerializer(profile).data
            except LorryOwnerProfile.DoesNotExist:
                pass
        elif user.role == User.BUSINESS:
            try:
                profile = user.business_profile
                data['profile'] = BusinessProfileSerializer(profile).data
            except BusinessProfile.DoesNotExist:
                pass
        
        return Response(data)
    

class APIRootView(APIView):
    def get(self, request):
        return Response({
            "token": "/auth/token/",
            "token_refresh": "/auth/token/refresh/",
            "register_driver": "/auth/register/driver/",
            "register_lorry_owner": "/auth/register/lorry-owner/",
            "register_business": "/auth/register/business/",
            "register_admin": "/auth/register/admin/",
            "profile": "/auth/profile/",
        })