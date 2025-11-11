from rest_framework import serializers
from .models import (
    HeroSection, FirstSection, SecondSection, SecondSectionCard,
    ThirdSection, ThirdSectionCard, FourthSectionGrowTogether
)


# ✅ универсальное поле, которое возвращает полный URL
class AbsoluteImageUrlField(serializers.ImageField):
    def to_representation(self, value):
        if not value:
            return None
        request = self.context.get("request")
        return request.build_absolute_uri(value.url)


# ✅ Hero
class HeroSectionSerializer(serializers.ModelSerializer):
    image = AbsoluteImageUrlField()

    class Meta:
        model = HeroSection
        fields = "__all__"


# ✅ First section
class FirstSectionSerializer(serializers.ModelSerializer):
    image = AbsoluteImageUrlField()

    class Meta:
        model = FirstSection
        fields = "__all__"


# ✅ Second section cards
class SecondSectionCardSerializer(serializers.ModelSerializer):
    cardIcon = AbsoluteImageUrlField()

    class Meta:
        model = SecondSectionCard
        fields = "__all__"


# ✅ Second section
class SecondSectionSerializer(serializers.ModelSerializer):
    cardInfo = SecondSectionCardSerializer(source='cards', many=True)

    class Meta:
        model = SecondSection
        fields = ("mainTitle", "cardInfo")


# ✅ Third section cards
class ThirdSectionCardSerializer(serializers.ModelSerializer):
    image = AbsoluteImageUrlField()

    class Meta:
        model = ThirdSectionCard
        fields = "__all__"


# ✅ Third section
class ThirdSectionSerializer(serializers.ModelSerializer):
    cards = ThirdSectionCardSerializer(many=True)

    class Meta:
        model = ThirdSection
        fields = "__all__"


# ✅ Fourth section
class FourthSectionGrowTogetherSerializer(serializers.ModelSerializer):
    image = AbsoluteImageUrlField()

    class Meta:
        model = FourthSectionGrowTogether
        fields = "__all__"
