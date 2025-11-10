from django.db import models

# Hero section
class QualityHeroSection(models.Model):
    title1 = models.CharField(max_length=200)
    mainTitleSpan1 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    mainTitleSpan2 = models.CharField(max_length=200)
    text = models.TextField()
    leftSideImage1 = models.ImageField(upload_to="quality/")
    leftSideImage2 = models.ImageField(upload_to="quality/")
    leftSideImage3 = models.ImageField(upload_to="quality/")
    rightSideImage = models.ImageField(upload_to="quality/")

# Second section
class QualitySecondSection(models.Model):
    image = models.ImageField(upload_to="quality/")
    title = models.CharField(max_length=200)
    titleSpan = models.CharField(max_length=200)
    text = models.TextField()

# Third section drops
class QualityThirdSectionDrop(models.Model):
    image = models.ImageField(upload_to="quality/")
    dropsTitle = models.CharField(max_length=200)
    dropsText = models.TextField()

class QualityThirdSection(models.Model):
    dropsList = models.ManyToManyField(QualityThirdSectionDrop, related_name="third_sections")

# Fourth section blocks
class QualityFourthSectionBlock(models.Model):
    key = models.CharField(max_length=50, unique=True)  # ensure, accountability, stewardship, certifications
    image = models.ImageField(upload_to="quality/")
    title = models.CharField(max_length=200)
    titleSpan = models.CharField(max_length=200, blank=True)
    text = models.TextField()
