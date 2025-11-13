from django.contrib import admin
from .models import (
    HeroSection, FirstSection, SecondSection, SecondSectionCard,
    ThirdSection, ThirdSectionCard, FourthSectionGrowTogether, Review
)

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ("mainTitle", "mainTitleSpan1", "mainTitleSpan2")
    exclude = ("title1", "title2", "mainTitle", "mainTitleSpan1", "mainTitleSpan2", "firstText", "secondText")
    

@admin.register(FirstSection)
class FirstSectionAdmin(admin.ModelAdmin):
    list_display = ("title",)
    exclude = ("title", "titleSpan", "text")

@admin.register(SecondSectionCard)
class SecondSectionCardAdmin(admin.ModelAdmin):
    list_display = ("title",)
    exclude = ("title", "text")

@admin.register(SecondSection)
class SecondSectionAdmin(admin.ModelAdmin):
    list_display = ("mainTitle",)
    filter_horizontal = ("cards",)

@admin.register(ThirdSectionCard)
class ThirdSectionCardAdmin(admin.ModelAdmin):
    list_display = ("text",)
    exclude = ("text",)

@admin.register(ThirdSection)
class ThirdSectionAdmin(admin.ModelAdmin):
    filter_horizontal = ("cards",)

@admin.register(FourthSectionGrowTogether)
class FourthSectionGrowTogetherAdmin(admin.ModelAdmin):
    list_display = ("title",)
    exclude = ("title", "titleSpan", "text")

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "preview", "video", "videoId")
