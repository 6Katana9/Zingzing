from modeltranslation.translator import register, TranslationOptions
from .models import ReachUsHeroSection, ReachUsSecondSection

# ✅ Hero section
@register(ReachUsHeroSection)
class ReachUsHeroSectionTranslationOptions(TranslationOptions):
    fields = (
        'mainTitle',
        'text',
    )

# ✅ Second section
@register(ReachUsSecondSection)
class ReachUsSecondSectionTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'text',
    )
