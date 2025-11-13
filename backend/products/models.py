from django.db import models

# Hero section
class HeroSection(models.Model):
    title1 = models.CharField(max_length=200)
    mainTitleSpan1 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    mainTitleSpan2 = models.CharField(max_length=200)
    leftSideImage = models.ImageField(upload_to="products/")
    rightSideImage1 = models.ImageField(upload_to="products/")
    rightSideImage2 = models.ImageField(upload_to="products/")
    rightSideImage3 = models.ImageField(upload_to="products/")


    def __str__(self):
        return self.title1

# Second section small cards
class SecondSectionSmallCard(models.Model):
    title = models.CharField(max_length=200)
    titleSpan = models.CharField(max_length=200)
    image = models.ImageField(upload_to="products/")


    def __str__(self):
        return self.title

class SecondSection(models.Model):
    cards = models.ManyToManyField(SecondSectionSmallCard, related_name="second_sections")

# Third section big cards
class ThirdSectionBigCard(models.Model):
    title = models.CharField(max_length=200)
    titleSpan = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to="products/")


    def __str__(self):
        return self.title

class ThirdSection(models.Model):
    bigCard = models.ManyToManyField(ThirdSectionBigCard, related_name="third_sections")

# Fourth section grow together
class FourthSectionGrowTogether(models.Model):
    image = models.ImageField(upload_to="products/")
    title = models.CharField(max_length=200)
    titleSpan = models.CharField(max_length=200)
    text = models.TextField()



    def __str__(self):
        return self.title