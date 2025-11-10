from rest_framework import serializers
from .models import (
    HeroSection, FirstSection, SecondSection, SecondSectionCard,
    ThirdSection, ThirdSectionCard, FourthSectionGrowTogether
)

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = "__all__"

class FirstSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstSection
        fields = "__all__"

class SecondSectionCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondSectionCard
        fields = "__all__"

class SecondSectionSerializer(serializers.ModelSerializer):
    cardInfo = SecondSectionCardSerializer(source='cards', many=True)
    class Meta:
        model = SecondSection
        fields = ("mainTitle", "cardInfo")

class ThirdSectionCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdSectionCard
        fields = "__all__"

class ThirdSectionSerializer(serializers.ModelSerializer):
    cards = ThirdSectionCardSerializer(many=True)
    class Meta:
        model = ThirdSection
        fields = "__all__"

class FourthSectionGrowTogetherSerializer(serializers.ModelSerializer):
    class Meta:
        model = FourthSectionGrowTogether
        fields = "__all__"
