from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, DriverProfile, LorryOwnerProfile, BusinessProfile


# Inline admin for Driver
class DriverProfileInline(admin.StackedInline):
    model = DriverProfile
    can_delete = False
    verbose_name_plural = 'Driver Profile'
    fk_name = 'user'


# Inline admin for Lorry Owner
class LorryOwnerProfileInline(admin.StackedInline):
    model = LorryOwnerProfile
    can_delete = False
    verbose_name_plural = 'Lorry Owner Profile'
    fk_name = 'user'


# Inline admin for Business
class BusinessProfileInline(admin.StackedInline):
    model = BusinessProfile
    can_delete = False
    verbose_name_plural = 'Business Profile'
    fk_name = 'user'


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'phone_number', 'username', 'role', 'is_staff', 'is_superuser')
    list_filter = ('role', 'is_staff', 'is_superuser')
    search_fields = ('phone_number', 'username')
    ordering = ('id',)

    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Personal Info', {'fields': ('username',)}),
        ('Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'username', 'password1', 'password2', 'role'),
        }),
    )

    inlines = []

    def get_inlines(self, request, obj):
        if not obj:
            return []

        if obj.role == User.DRIVER:
            return [DriverProfileInline]
        elif obj.role == User.LORRY_OWNER:
            return [LorryOwnerProfileInline]
        elif obj.role == User.BUSINESS:
            return [BusinessProfileInline]
        return []

    def get_inline_instances(self, request, obj=None):
        inline_instances = []
        for inline_class in self.get_inlines(request, obj):
            inline = inline_class(self.model, self.admin_site)
            inline_instances.append(inline)
        return inline_instances


# Register profile models separately as well (optional but useful)
@admin.register(DriverProfile)
class DriverProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'license_number', 'driving_experience', 'vehicle_type')


@admin.register(LorryOwnerProfile)
class LorryOwnerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'number_of_vehicles', 'business_registration_number')


@admin.register(BusinessProfile)
class BusinessProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'business_name', 'business_type', 'address')