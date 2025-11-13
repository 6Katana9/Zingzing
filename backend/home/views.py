from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import HeroSection, FirstSection, SecondSection, ThirdSection, FourthSectionGrowTogether, Review
from .serializers import (
    HeroSectionSerializer, FirstSectionSerializer, SecondSectionSerializer,
    ThirdSectionSerializer, FourthSectionGrowTogetherSerializer, ReviewSerializer
)



@api_view(['GET'])
def products_home(request):
    hero = HeroSection.objects.first()
    first_section = FirstSection.objects.first()
    second_section = SecondSection.objects.first()
    third_section = ThirdSection.objects.first()
    fourth_section = FourthSectionGrowTogether.objects.first()
    reviews = Review.objects.all()

    return Response({
        "hero": HeroSectionSerializer(hero, context={"request": request}).data if hero else {},
        "firstSection": FirstSectionSerializer(first_section, context={"request": request}).data if first_section else {},
        "secondSection": SecondSectionSerializer(second_section, context={"request": request}).data if second_section else {},
        "thirdSection": ThirdSectionSerializer(third_section, context={"request": request}).data if third_section else {},
        "fourthSectionGrowTogether": FourthSectionGrowTogetherSerializer(fourth_section, context={"request": request}).data if fourth_section else {},
        "reviews": ReviewSerializer(reviews, many=True, context={"request": request}).data
    })