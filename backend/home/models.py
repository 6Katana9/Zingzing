from django.db import models

# Hero section
class HeroSection(models.Model):
    mainTitle = models.CharField(max_length=200)
    mainTitleSpan1 = models.CharField(max_length=200)
    mainTitleSpan2 = models.CharField(max_length=200)
    firstText = models.TextField()
    image = models.ImageField(upload_to="products/")
    secondText = models.TextField()


    def __str__(self):
        return self.mainTitle

# First section
class FirstSection(models.Model):
    image = models.ImageField(upload_to="products/")
    title = models.CharField(max_length=200)
    titleSpan = models.CharField(max_length=200, blank=True)
    text = models.TextField()


    def __str__(self):
        return self.title

# Second section card
class SecondSectionCard(models.Model):
    cardIcon = models.ImageField(upload_to="products/")
    title = models.CharField(max_length=200)
    text = models.TextField()


    def __str__(self):
        return self.title

class SecondSection(models.Model):
    mainTitle = models.CharField(max_length=200)
    # Связь с карточками
    cards = models.ManyToManyField(SecondSectionCard, related_name="second_sections")


    def __str__(self):
        return self.mainTitle

# Third section card
class ThirdSectionCard(models.Model):
    image = models.ImageField(upload_to="products/")
    text = models.TextField()


    def __str__(self):
        return self.text

class ThirdSection(models.Model):
    cards = models.ManyToManyField(ThirdSectionCard, related_name="third_sections")



# Fourth section
class FourthSectionGrowTogether(models.Model):
    image = models.ImageField(upload_to="products/")
    title = models.CharField(max_length=200)
    titleSpan = models.CharField(max_length=200, blank=True)
    text = models.TextField()


    def __str__(self):
        return self.title