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

    return Response({
        "hero": HeroSectionSerializer(hero).data if hero else {},
        "secondSectionSmallCard": SecondSectionSerializer(second_section).data if second_section else {},
        "thirdSectionBigCards": ThirdSectionSerializer(third_section).data if third_section else {},
        "fourthSectionGrowTogether": FourthSectionGrowTogetherSerializer(fourth_section).data if fourth_section else {}
    })
