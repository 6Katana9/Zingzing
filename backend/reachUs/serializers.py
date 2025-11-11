from rest_framework import serializers
from .models import ReachUsHeroSection, ReachUsSecondSection
from home.serializers import AbsoluteImageUrlField

class ReachUsHeroSectionSerializer(serializers.ModelSerializer):
    image = AbsoluteImageUrlField()  # замените на реальное имя поля картинки, если отличается

    class Meta:
        model = ReachUsHeroSection
        fields = "__all__"


# ✅ Reach Us Second Section
class ReachUsSecondSectionSerializer(serializers.ModelSerializer):
    image = AbsoluteImageUrlField()  # замените на реальное имя поля картинки, если отличается

    class Meta:
        model = ReachUsSecondSection
        fields = "__all__"