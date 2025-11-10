from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import HeroSection, FirstSection, SecondSection, ThirdSection, FourthSectionGrowTogether
from .serializers import (
    HeroSectionSerializer, FirstSectionSerializer, SecondSectionSerializer,
    ThirdSectionSerializer, FourthSectionGrowTogetherSerializer
)

@api_view(['GET'])
def products_home(request):
    hero = HeroSection.objects.first()
    first_section = FirstSection.objects.first()
    second_section = SecondSection.objects.first()
    third_section = ThirdSection.objects.first()
    fourth_section = FourthSectionGrowTogether.objects.first()

    return Response({
        "hero": HeroSectionSerializer(hero).data if hero else {},
        "firstSection": FirstSectionSerializer(first_section).data if first_section else {},
        "secondSection": SecondSectionSerializer(second_section).data if second_section else {},
        "thirdSection": ThirdSectionSerializer(third_section).data if third_section else {},
        "fourthSectionGrowTogether": FourthSectionGrowTogetherSerializer(fourth_section).data if fourth_section else {}
    })
