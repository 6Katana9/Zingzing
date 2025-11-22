from django.db import models

# Hero section
class HeroSection(models.Model):
    title1 = models.CharField(max_length=200, blank=True, null=True)
    title2 = models.CharField(max_length=200, blank=True, null=True)
    mainTitle = models.CharField(max_length=200, blank=True, null=True)
    mainTitleSpan1 = models.CharField(max_length=200, blank=True, null=True)
    mainTitleSpan2 = models.CharField(max_length=200, blank=True, null=True)
    firstText = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="products/")
    secondText = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.mainTitle

# First section
class FirstSection(models.Model):
    image = models.ImageField(upload_to="products/")
    title = models.CharField(max_length=200, blank=True, null=True)
    titleSpan = models.CharField(max_length=200, blank=True)
    text = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.title

# Second section card
class SecondSectionCard(models.Model):
    cardIcon = models.ImageField(upload_to="products/")
    title = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.title

class SecondSection(models.Model):
    mainTitle = models.CharField(max_length=200, blank=True, null=True)
    # Связь с карточками
    cards = models.ManyToManyField(SecondSectionCard, related_name="second_sections")


    def __str__(self):
        return self.mainTitle

# Third section card
class ThirdSectionCard(models.Model):
    image = models.ImageField(upload_to="products/")
    text = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.text

class ThirdSection(models.Model):
    cards = models.ManyToManyField(ThirdSectionCard, related_name="third_sections")



# Fourth section
class FourthSectionGrowTogether(models.Model):
    image = models.ImageField(upload_to="products/")
    title = models.CharField(max_length=200, blank=True, null=True)
    titleSpan = models.CharField(max_length=200, blank=True)
    text = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.title
    

class Review(models.Model):
    preview = models.ImageField(upload_to="reviews/")
    video = models.FileField(upload_to="videos/", blank=True, null=True)
    videoId = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Review {self.id}"
