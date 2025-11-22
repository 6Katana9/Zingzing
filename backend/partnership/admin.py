from django.contrib import admin
from .models import PartnershipRequest


@admin.register(PartnershipRequest)
class PartnershipRequestAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'created_at')
    search_fields = ('email', 'phone_number')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
