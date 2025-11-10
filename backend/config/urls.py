from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Zingzing DOCS",
        default_version="v1",
        description="Swagger for front"
    ),
    public=False,
    # permission_classes=[permissions.IsAdminUser],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('aboutUs/', include('aboutUs.urls')),
    path('factory/', include('factory.urls')),
    path('home/', include('home.urls')),
    path('news/', include('news.urls')),
    path('products/', include('products.urls')),
    path('quality/', include('quality.urls')),
    path('reachUs/', include('reachUs.urls')),

    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)