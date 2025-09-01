from django.contrib import admin
from .models import Load

@admin.register(Load)
class LoadAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'source', 'destination', 'weight', 'material_type', 'pickup_date', 'created_at')
    list_filter = ('source', 'destination', 'pickup_date')
    search_fields = ('source', 'destination', 'material_type', 'user__username')
    ordering = ('-created_at',)