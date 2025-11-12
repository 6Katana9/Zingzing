from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import HeroSection, SecondSection, ThirdSection, FourthSectionGrowTogether
from .serializers import (
    HeroSectionSerializer, SecondSectionSerializer,
    ThirdSectionSerializer, FourthSectionGrowTogetherSerializer
)

@api_view(['GET'])
def products_page(request):
    hero = HeroSection.objects.first()
    second_section = SecondSection.objects.first()
    third_section = ThirdSection.objects.first()
    fourth_section = FourthSectionGrowTogether.objects.first()

    hero_data = HeroSectionSerializer(hero, context={"request": request}).data if hero else {}
    second_data = SecondSectionSerializer(second_section, context={"request": request}).data if second_section else {}
    third_data = ThirdSectionSerializer(third_section, context={"request": request}).data if third_section else {}
    fourth_data = FourthSectionGrowTogetherSerializer(fourth_section, context={"request": request}).data if fourth_section else {}

    return Response({
        "hero": hero_data,
        "secondSectionSmallCard": second_data,
        "thirdSectionBigCards": third_data,
        "fourthSectionGrowTogether": fourth_data
    })
