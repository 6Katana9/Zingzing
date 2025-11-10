from django.contrib import admin
from .models import (
    HeroSection, SecondSection, CountryItem, DropsItem,
    ThirdSection, ThirdBlock
)


class CountryInline(admin.TabularInline):
    model = CountryItem
    extra = 0


class DropsInline(admin.TabularInline):
    model = DropsItem
    extra = 0


@admin.register(SecondSection)
class SecondSectionAdmin(admin.ModelAdmin):
    inlines = [CountryInline, DropsInline]


class ThirdBlockInline(admin.TabularInline):
    model = ThirdBlock
    extra = 0


@admin.register(ThirdSection)
class ThirdSectionAdmin(admin.ModelAdmin):
    inlines = [ThirdBlockInline]


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ("title1", "mainTitleSpan1")
