from django.contrib import admin
from .models import (
    HeroSection, SecondSection, SecondSectionSmallCard,
    ThirdSection, ThirdSectionBigCard, ThirdSection, FourthSectionGrowTogether, LittleImages
)

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ("title1", "mainTitleSpan1", "title2", "mainTitleSpan2")
    exclude = ("title1", "mainTitleSpan1", "title2", "mainTitleSpan2")


@admin.register(LittleImages)
class LittleImagesAdmin(admin.ModelAdmin):
    list_display = ("image",)

@admin.register(SecondSectionSmallCard)
class SecondSectionSmallCardAdmin(admin.ModelAdmin):
    list_display = ("title", "titleSpan")
    exclude = ("title", "titleSpan")
    filter_horizontal = ("littleImages",)  # <-- это позволит выбирать несколько картинок удобным виджетом


@admin.register(SecondSection)
class SecondSectionAdmin(admin.ModelAdmin):
    filter_horizontal = ("cards",)

@admin.register(ThirdSectionBigCard)
class ThirdSectionBigCardAdmin(admin.ModelAdmin):
    list_display = ("title", "titleSpan")
    exclude = ("title", "titleSpan", "text")

@admin.register(ThirdSection)
class ThirdSectionAdmin(admin.ModelAdmin):
    filter_horizontal = ("bigCard",)

@admin.register(FourthSectionGrowTogether)
class FourthSectionGrowTogetherAdmin(admin.ModelAdmin):
    list_display = ("title", "titleSpan")
    exclude = ("title", "titleSpan", "text")
