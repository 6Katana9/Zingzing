from django.db import models

# Hero section
class HeroSection(models.Model):
    title1 = models.CharField(max_length=200, blank=True, null=True)
    mainTitleSpan1 = models.CharField(max_length=200, blank=True, null=True)
    title2 = models.CharField(max_length=200, blank=True, null=True)
    mainTitleSpan2 = models.CharField(max_length=200, blank=True, null=True)
    leftSideImage = models.ImageField(upload_to="products/")
    rightSideImage1 = models.ImageField(upload_to="products/")
    rightSideImage2 = models.ImageField(upload_to="products/")
    rightSideImage3 = models.ImageField(upload_to="products/")


    def __str__(self):
        return self.title1


class LittleImages(models.Model):
    image = models.ImageField(upload_to="products/")

# Second section small cards
class SecondSectionSmallCard(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    titleSpan = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="products/")
    littleImages = models.ForeignKey(LittleImages, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
    
class SecondSection(models.Model):
    cards = models.ManyToManyField(SecondSectionSmallCard, related_name="second_sections")

# Third section big cards
class ThirdSectionBigCard(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    titleSpan = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="products/")


    def __str__(self):
        return self.title

class ThirdSection(models.Model):
    bigCard = models.ManyToManyField(ThirdSectionBigCard, related_name="third_sections")

# Fourth section grow together
class FourthSectionGrowTogether(models.Model):
    image = models.ImageField(upload_to="products/")
    title = models.CharField(max_length=200, blank=True, null=True)
    titleSpan = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title