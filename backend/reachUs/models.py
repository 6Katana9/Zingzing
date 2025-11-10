from django.db import models

# Hero section
class ReachUsHeroSection(models.Model):
    mainTitle = models.CharField(max_length=200)
    text = models.TextField()
    leftSideImage1 = models.ImageField(upload_to="reachus/")
    leftSideImage2 = models.ImageField(upload_to="reachus/")
    leftSideImage3 = models.ImageField(upload_to="reachus/")
    rightSideImage = models.ImageField(upload_to="reachus/")

# Second section
class ReachUsSecondSection(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to="reachus/")
