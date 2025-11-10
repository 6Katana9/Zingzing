from rest_framework import serializers
from .models import (
    QualityHeroSection, QualitySecondSection,
    QualityThirdSection, QualityThirdSectionDrop,
    QualityFourthSectionBlock
)

class QualityHeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityHeroSection
        fields = "__all__"

class QualitySecondSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualitySecondSection
        fields = "__all__"

class QualityThirdSectionDropSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityThirdSectionDrop
        fields = "__all__"

class QualityThirdSectionSerializer(serializers.ModelSerializer):
    dropsList = QualityThirdSectionDropSerializer(many=True)
    class Meta:
        model = QualityThirdSection
        fields = ("dropsList",)

class QualityFourthSectionBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityFourthSectionBlock
        fields = "__all__"
