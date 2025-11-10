from rest_framework import serializers
from .models import (
    HeroSection, SecondSection, SecondSectionSmallCard,
    ThirdSection, ThirdSectionBigCard, FourthSectionGrowTogether
)

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = "__all__"

class SecondSectionSmallCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondSectionSmallCard
        fields = "__all__"

class SecondSectionSerializer(serializers.ModelSerializer):
    cards = SecondSectionSmallCardSerializer(many=True)
    class Meta:
        model = SecondSection
        fields = ("cards",)

class ThirdSectionBigCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdSectionBigCard
        fields = "__all__"

class ThirdSectionSerializer(serializers.ModelSerializer):
    bigCard = ThirdSectionBigCardSerializer(many=True)
    class Meta:
        model = ThirdSection
        fields = ("bigCard",)

class FourthSectionGrowTogetherSerializer(serializers.ModelSerializer):
    class Meta:
        model = FourthSectionGrowTogether
        fields = "__all__"
