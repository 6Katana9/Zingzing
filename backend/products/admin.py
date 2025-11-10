from django.contrib import admin
from .models import (
    HeroSection, SecondSection, SecondSectionSmallCard,
    ThirdSection, ThirdSectionBigCard, ThirdSection, FourthSectionGrowTogether
)

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ("title1", "mainTitleSpan1", "title2", "mainTitleSpan2")
    fields = ("title1", "mainTitleSpan1", "title2", "mainTitleSpan2",
              "leftSideImage", "rightSideImage1", "rightSideImage2", "rightSideImage3")

@admin.register(SecondSectionSmallCard)
class SecondSectionSmallCardAdmin(admin.ModelAdmin):
    list_display = ("title", "titleSpan")
    fields = ("title", "titleSpan", "image")

@admin.register(SecondSection)
class SecondSectionAdmin(admin.ModelAdmin):
    filter_horizontal = ("cards",)

@admin.register(ThirdSectionBigCard)
class ThirdSectionBigCardAdmin(admin.ModelAdmin):
    list_display = ("title", "titleSpan")
    fields = ("title", "titleSpan", "text", "image")

@admin.register(ThirdSection)
class ThirdSectionAdmin(admin.ModelAdmin):
    filter_horizontal = ("bigCard",)

@admin.register(FourthSectionGrowTogether)
class FourthSectionGrowTogetherAdmin(admin.ModelAdmin):
    list_display = ("title", "titleSpan")
    fields = ("image", "title", "titleSpan", "text")
