from rest_framework import serializers
from .models import HeroSection, Section, SwiperSlide
from home.serializers import AbsoluteImageUrlField


# ✅ HeroSection
class HeroSectionSerializer(serializers.ModelSerializer):
    image1 = AbsoluteImageUrlField()
    image2 = AbsoluteImageUrlField()
    image3 = AbsoluteImageUrlField()

    class Meta:
        model = HeroSection
        fields = "__all__"


# ✅ Section
class SectionSerializer(serializers.ModelSerializer):
    image = AbsoluteImageUrlField()

    class Meta:
        model = Section
        fields = "__all__"


# ✅ SwiperSlide
class SwiperSlideSerializer(serializers.ModelSerializer):
    image = AbsoluteImageUrlField()

    class Meta:
        model = SwiperSlide
        fields = "__all__"
