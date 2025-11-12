from modeltranslation.translator import register, TranslationOptions
from .models import HeroSection, Section, SwiperSlide

# ✅ HeroSection
@register(HeroSection)
class HeroSectionTranslationOptions(TranslationOptions):
    fields = (
        'title1',
        'titleSpan1',
        'title2',
        'titleSpan2',
        'text',
    )

# ✅ Section
@register(Section)
class SectionTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'text',
    )

# ✅ SwiperSlide
@register(SwiperSlide)
class SwiperSlideTranslationOptions(TranslationOptions):
    fields = (
        'alt',
    )
