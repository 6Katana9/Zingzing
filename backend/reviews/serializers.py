from rest_framework import serializers
from .models import VideoReviews

class VideoReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoReviews
        fields = '__all__'