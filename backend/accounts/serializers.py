from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import DriverProfile, LorryOwnerProfile, BusinessProfile

User = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Add custom claims
        token['username'] = user.username
        token['role'] = user.role
        
        return token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'role')
        read_only_fields = ('id', 'role')

class DriverProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverProfile
        fields = ('license_number', 'driving_experience', 'vehicle_type')

class LorryOwnerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LorryOwnerProfile
        fields = ('company_name', 'number_of_vehicles', 'business_registration_number')

class BusinessProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProfile
        fields = ('business_name', 'business_type', 'address')

class DriverRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = DriverProfileSerializer()
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'profile')
    
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        validated_data['role'] = User.DRIVER
        
        user = User.objects.create_user(**validated_data)
        DriverProfile.objects.create(user=user, **profile_data)
        
        return user

class LorryOwnerRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = LorryOwnerProfileSerializer()
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'profile')
    
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        validated_data['role'] = User.LORRY_OWNER
        
        user = User.objects.create_user(**validated_data)
        LorryOwnerProfile.objects.create(user=user, **profile_data)
        
        return user

class BusinessRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = BusinessProfileSerializer()
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'profile')
    
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        validated_data['role'] = User.BUSINESS
        
        user = User.objects.create_user(**validated_data)
        BusinessProfile.objects.create(user=user, **profile_data)
        
        return user

class AdminRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'phone_number')
    
    def create(self, validated_data):
        validated_data['role'] = User.ADMIN
        validated_data['is_staff'] = True
        
        user = User.objects.create_user(**validated_data)
        return user