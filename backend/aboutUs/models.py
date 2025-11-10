from django.db import models

class HeroSection(models.Model):
    title1 = models.CharField(max_length=255)
    mainTitleSpan1 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    mainTitleSpan2 = models.CharField(max_length=255)
    text = models.TextField()

    leftSideImage1 = models.ImageField(upload_to="about/hero/")
    leftSideImage2 = models.ImageField(upload_to="about/hero/")
    leftSideImage3 = models.ImageField(upload_to="about/hero/")
    rightSideImage = models.ImageField(upload_to="about/hero/")

    def __str__(self):
        return "Hero Section"


class CountryItem(models.Model):
    section = models.ForeignKey(
        "SecondSection",
        related_name="list",
        on_delete=models.CASCADE
    )

    image = models.ImageField(upload_to="about/countries/")
    innerTitle = models.CharField(max_length=255)
    text = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return self.innerTitle


class DropsItem(models.Model):
    section = models.ForeignKey(
        "SecondSection",
        related_name="dropsList",
        on_delete=models.CASCADE
    )

    image = models.ImageField(upload_to="about/drops/")
    dropsTitle = models.CharField(max_length=255)
    dropsText = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return self.dropsTitle


class SecondSection(models.Model):
    mainTitle = models.CharField(max_length=255)
    mainTitleSpan = models.CharField(max_length=255)

    def __str__(self):
        return "Second Section"


class ThirdSection(models.Model):
    def __str__(self):
        return "Third Section"

class ThirdBlock(models.Model):
    section = models.ForeignKey(
        ThirdSection,
        related_name="blocks",
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=255)
    titleSpan = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to="about/third/")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return f"{self.title} {self.titleSpan}"
