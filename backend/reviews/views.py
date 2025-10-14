from rest_framework import generics
from .models import VideoReviews
from .serializers import VideoReviewsSerializer


class VideoReviewsListAPIView(generics.ListAPIView):
    queryset = VideoReviews.objects.all().order_by('-created_at')
    serializer_class = VideoReviewsSerializer


class VideoReviewsDetailAPIView(generics.RetrieveAPIView):
    queryset = VideoReviews.objects.all()
    serializer_class = VideoReviewsSerializer
    lookup_field = 'pk'
