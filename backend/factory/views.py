from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import HeroSection, Section, SwiperSlide
from .serializers import HeroSectionSerializer, SectionSerializer, SwiperSlideSerializer

@api_view(['GET'])
def factory_page(request):
    hero = HeroSection.objects.first()
    hero_data = HeroSectionSerializer(hero).data if hero else {}

    sections = Section.objects.all()
    sections_data = {section.key: SectionSerializer(section).data for section in sections}

    slides = SwiperSlide.objects.all()
    slides_data = SwiperSlideSerializer(slides, many=True).data

    return Response({
        "hero": hero_data,
        **sections_data,
        "swiper": {
            "slides": slides_data
        }
    })
