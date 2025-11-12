from django.contrib import admin
from .models import (
    HeroSection, SecondSection, CountryItem, DropsItem,
    ThirdSection, ThirdBlock
)


class CountryInline(admin.TabularInline):
    model = CountryItem
    extra = 0
    exclude = (
        'innerTitle',
        'text',
    )

class DropsInline(admin.TabularInline):
    model = DropsItem
    extra = 0
    exclude = (
        'dropsTitle',
        'dropsText',
    )

@admin.register(SecondSection)
class SecondSectionAdmin(admin.ModelAdmin):
    inlines = [CountryInline, DropsInline]
    exclude = (
        'mainTitle',
        'mainTitleSpan',
    )

class ThirdBlockInline(admin.TabularInline):
    model = ThirdBlock
    extra = 0
    exclude = (
        'title',
        'titleSpan',
        'text',
    )

@admin.register(ThirdSection)
class ThirdSectionAdmin(admin.ModelAdmin):
    inlines = [ThirdBlockInline]


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ("title1", "mainTitleSpan1")
    exclude = (
        'title1',
        'mainTitleSpan1',
        'title2',
        'mainTitleSpan2',
        'text',
    )
