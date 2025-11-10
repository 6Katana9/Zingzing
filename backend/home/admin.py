from django.contrib import admin
from .models import (
    HeroSection, FirstSection, SecondSection, SecondSectionCard,
    ThirdSection, ThirdSectionCard, FourthSectionGrowTogether
)

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ("mainTitle", "mainTitleSpan1", "mainTitleSpan2")
    fields = ("mainTitle", "mainTitleSpan1", "mainTitleSpan2", "firstText", "image", "secondText")

@admin.register(FirstSection)
class FirstSectionAdmin(admin.ModelAdmin):
    list_display = ("title",)
    fields = ("image", "title", "titleSpan", "text")

@admin.register(SecondSectionCard)
class SecondSectionCardAdmin(admin.ModelAdmin):
    list_display = ("title",)
    fields = ("cardIcon", "title", "text")

@admin.register(SecondSection)
class SecondSectionAdmin(admin.ModelAdmin):
    list_display = ("mainTitle",)
    filter_horizontal = ("cards",)

@admin.register(ThirdSectionCard)
class ThirdSectionCardAdmin(admin.ModelAdmin):
    list_display = ("text",)
    fields = ("image", "text")

@admin.register(ThirdSection)
class ThirdSectionAdmin(admin.ModelAdmin):
    filter_horizontal = ("cards",)

@admin.register(FourthSectionGrowTogether)
class FourthSectionGrowTogetherAdmin(admin.ModelAdmin):
    list_display = ("title",)
    fields = ("image", "title", "titleSpan", "text")
