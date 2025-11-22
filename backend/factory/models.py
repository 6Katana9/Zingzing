from django.db import models

class HeroSection(models.Model):
    title1 = models.CharField(max_length=200, blank=True, null=True)
    titleSpan1 = models.CharField(max_length=200, blank=True, null=True)
    title2 = models.CharField(max_length=200, blank=True, null=True)
    titleSpan2 = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to="factory/")
    image2 = models.ImageField(upload_to="factory/")
    image3 = models.ImageField(upload_to="factory/")


    def __str__(self):
        return self.title1

class Section(models.Model):
    key = models.CharField(max_length=50, unique=True)  # "secondSection", "thirdSection", "fourthSection"
    title = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="factory/")


    def __str__(self):
        return self.title

class SwiperSlide(models.Model):
    image = models.ImageField(upload_to="factory/")
    alt = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return self.alt