# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User, DriverProfile, LorryOwnerProfile, BusinessProfile

class DriverProfileInline(admin.StackedInline):
    model = DriverProfile
    can_delete = False
    verbose_name_plural = 'Driver Profile'

class LorryOwnerProfileInline(admin.StackedInline):
    model = LorryOwnerProfile
    can_delete = False
    verbose_name_plural = 'Lorry Owner Profile'

class BusinessProfileInline(admin.StackedInline):
    model = BusinessProfile
    can_delete = False
    verbose_name_plural = 'Business Profile'

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone_number')}),
        (_('Role'), {'fields': ('role',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'role', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    
    def get_inlines(self, request, obj=None):
        if obj:
            if obj.role == User.DRIVER:
                return [DriverProfileInline]
            elif obj.role == User.LORRY_OWNER:
                return [LorryOwnerProfileInline]
            elif obj.role == User.BUSINESS:
                return [BusinessProfileInline]
        return []

# Register the models
admin.site.register(User, CustomUserAdmin)
admin.site.register(DriverProfile)
admin.site.register(LorryOwnerProfile)
admin.site.register(BusinessProfile)