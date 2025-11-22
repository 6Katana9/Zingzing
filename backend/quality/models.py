from django.db import models

# Hero section
class QualityHeroSection(models.Model):
    title1 = models.CharField(max_length=200, blank=True, null=True)
    mainTitleSpan1 = models.CharField(max_length=200, blank=True, null=True)
    title2 = models.CharField(max_length=200, blank=True, null=True)
    mainTitleSpan2 = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    leftSideImage1 = models.ImageField(upload_to="quality/")
    leftSideImage2 = models.ImageField(upload_to="quality/")
    leftSideImage3 = models.ImageField(upload_to="quality/")
    rightSideImage = models.ImageField(upload_to="quality/")

    def __str__(self):
        return self.title1

# Second section
class QualitySecondSection(models.Model):
    image = models.ImageField(upload_to="quality/")
    title = models.CharField(max_length=200, blank=True, null=True)
    titleSpan = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.title

# Third section drops
class QualityThirdSectionDrop(models.Model):
    image = models.ImageField(upload_to="quality/")
    dropsTitle = models.CharField(max_length=200, blank=True, null=True)
    dropsText = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.dropsTitle

class QualityThirdSection(models.Model):
    dropsList = models.ManyToManyField(QualityThirdSectionDrop, related_name="third_sections")

# Fourth section blocks
class QualityFourthSectionBlock(models.Model):
    key = models.CharField(max_length=50, unique=True)  # ensure, accountability, stewardship, certifications
    image = models.ImageField(upload_to="quality/")
    title = models.CharField(max_length=200, blank=True, null=True)
    titleSpan = models.CharField(max_length=200, blank=True)
    text = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.title