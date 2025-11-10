from django.db import models

class HeroSection(models.Model):
    title1 = models.CharField(max_length=200)
    titleSpan1 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    titleSpan2 = models.CharField(max_length=200)
    text = models.TextField()
    image1 = models.ImageField(upload_to="factory/")
    image2 = models.ImageField(upload_to="factory/")
    image3 = models.ImageField(upload_to="factory/")

class Section(models.Model):
    key = models.CharField(max_length=50, unique=True)  # "secondSection", "thirdSection", "fourthSection"
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to="factory/")

class SwiperSlide(models.Model):
    image = models.ImageField(upload_to="factory/")
    alt = models.CharField(max_length=200)
