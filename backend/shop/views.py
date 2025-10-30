from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Page
from .serializers import PageSerializer


class PageDetailBySlugView(generics.RetrieveAPIView):
    serializer_class = PageSerializer
    lookup_field = "slug"
    queryset = Page.objects.all()

    def get(self, request, *args, **kwargs):
        slug = kwargs.get("slug")
        try:
            page = Page.objects.get(slug=slug)
        except Page.DoesNotExist:
            raise NotFound("Страница не найдена")

        serializer = self.get_serializer(page)
        return Response(serializer.data)
