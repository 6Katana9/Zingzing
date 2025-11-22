from rest_framework import serializers
from .models import PartnershipRequest


class PartnershipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipRequest
        fields = ['id', 'email', 'phone', 'message', 'created_at']
        read_only_fields = ['id', 'created_at']
