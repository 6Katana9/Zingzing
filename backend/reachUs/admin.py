from django.contrib import admin
from .models import ReachUsHeroSection, ReachUsSecondSection

@admin.register(ReachUsHeroSection)
class ReachUsHeroSectionAdmin(admin.ModelAdmin):
    list_display = ("mainTitle",)
    fields = ("mainTitle", "text", "leftSideImage1", "leftSideImage2", "leftSideImage3", "rightSideImage")

@admin.register(ReachUsSecondSection)
class ReachUsSecondSectionAdmin(admin.ModelAdmin):
    list_display = ("title",)
    fields = ("title", "text", "image")
