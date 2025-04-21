from rest_framework import permissions

class IsLorryOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'lorry_owner'