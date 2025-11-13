from django.db import models

# Hero section
class NewsHeroSection(models.Model):
    mainTitle = models.CharField(max_length=200)
    titleSpan1 = models.CharField(max_length=200)
    titleSpan2 = models.CharField(max_length=200)
    text = models.TextField()
    leftSideImage1 = models.ImageField(upload_to="news/")
    leftSideImage2 = models.ImageField(upload_to="news/")
    leftSideImage3 = models.ImageField(upload_to="news/")
    rightSideImage = models.ImageField(upload_to="news/")


    def __str__(self):
        return self.mainTitle

# Second section blocks
class NewsSecondBlock(models.Model):
    title = models.CharField(max_length=200, blank=True)
    titleSpan = models.CharField(max_length=200, blank=True)
    text = models.TextField()
    image = models.ImageField(upload_to="news/")


    def __str__(self):
        return self.title

class NewsSecondSection(models.Model):
    firstBlock = models.OneToOneField(NewsSecondBlock, related_name="first_block", on_delete=models.CASCADE)
    secondBlock = models.OneToOneField(NewsSecondBlock, related_name="second_block", on_delete=models.CASCADE)
    thirdBlock = models.OneToOneField(NewsSecondBlock, related_name="third_block", on_delete=models.CASCADE)
