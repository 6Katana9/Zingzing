from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import HeroSection, Section, SwiperSlide
from .serializers import HeroSectionSerializer, SectionSerializer, SwiperSlideSerializer

@api_view(['GET'])
def factory_page(request):
    # Hero section
    hero = HeroSection.objects.first()
    hero_data = HeroSectionSerializer(hero, context={"request": request}).data if hero else {}

    # Other sections (keyed by section.key)
    sections = Section.objects.all()
    sections_data = {section.key: SectionSerializer(section, context={"request": request}).data for section in sections}

    # Swiper slides
    slides = SwiperSlide.objects.all()
    slides_data = SwiperSlideSerializer(slides, many=True, context={"request": request}).data

    return Response({
        "hero": hero_data,
        **sections_data,
        "swiper": {
            "slides": slides_data
        }
    })
