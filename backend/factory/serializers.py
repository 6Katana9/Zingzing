from rest_framework import serializers
from .models import HeroSection, Section, SwiperSlide

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = "__all__"

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"

class SwiperSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwiperSlide
        fields = "__all__"
