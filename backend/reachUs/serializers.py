from rest_framework import serializers
from .models import ReachUsHeroSection, ReachUsSecondSection

class ReachUsHeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReachUsHeroSection
        fields = "__all__"

class ReachUsSecondSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReachUsSecondSection
        fields = "__all__"
