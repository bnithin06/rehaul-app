from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import APIRootView, CustomTokenObtainPairView,UserRegistrationView

urlpatterns = [
    path('', APIRootView.as_view(), name='api-root'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationView.as_view(), name='register'),
]