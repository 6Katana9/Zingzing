from modeltranslation.translator import register, TranslationOptions
from .models import (
    QualityHeroSection, QualitySecondSection,
    QualityThirdSectionDrop, QualityFourthSectionBlock
)

# ✅ Hero section
@register(QualityHeroSection)
class QualityHeroSectionTranslationOptions(TranslationOptions):
    fields = (
        'title1',
        'mainTitleSpan1',
        'title2',
        'mainTitleSpan2',
        'text',
    )

# ✅ Second section
@register(QualitySecondSection)
class QualitySecondSectionTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'titleSpan',
        'text',
    )

# ✅ Third section drops
@register(QualityThirdSectionDrop)
class QualityThirdSectionDropTranslationOptions(TranslationOptions):
    fields = (
        'dropsTitle',
        'dropsText',
    )

# ✅ Fourth section blocks
@register(QualityFourthSectionBlock)
class QualityFourthSectionBlockTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'titleSpan',
        'text',
    )
