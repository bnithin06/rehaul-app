from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    CustomTokenObtainPairView, DriverRegistrationView, 
    LorryOwnerRegistrationView, BusinessRegistrationView,
    AdminRegistrationView, UserListView, UserProfileView,APIRootView
)

urlpatterns = [
    path('', APIRootView.as_view(), name='api_root'),
    # Authentication endpoints
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Registration endpoints
    path('register/driver/', DriverRegistrationView.as_view(), name='driver_register'),
    path('register/lorry-owner/', LorryOwnerRegistrationView.as_view(), name='lorry_owner_register'),
    path('register/business/', BusinessRegistrationView.as_view(), name='business_register'),
    path('register/admin/', AdminRegistrationView.as_view(), name='admin_register'),
    
    # User profile endpoint
    path('profile/', UserProfileView.as_view(), name='user_profile'),
     path('users/', UserListView.as_view(), name='user-list'),
]