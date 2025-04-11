from rest_framework.permissions import BasePermission

class IsDriver(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'driver'

class IsLorryOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'lorry_owner'

class IsBusiness(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'business'

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'