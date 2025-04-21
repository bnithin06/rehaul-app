from django.contrib import admin
from .models import LoadRequest

@admin.register(LoadRequest)
class LoadRequestAdmin(admin.ModelAdmin):
    list_display = ('posted_by', 'goods_type', 'source_location', 'destination_location', 'required_date', 'urgency')
    search_fields = ('posted_by__phone_number', 'goods_type')
    list_filter = ('urgency', 'required_date')