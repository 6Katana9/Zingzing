from django.urls import path
from .views import VideoReviewsListAPIView, VideoReviewsDetailAPIView

urlpatterns = [
    path('video-reviews/', VideoReviewsListAPIView.as_view(), name='video-reviews-list'),
    path('video-reviews/<int:pk>/', VideoReviewsDetailAPIView.as_view(), name='video-reviews-detail'),
]
