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
    path('api/admin/', admin.site.urls),

    path('api/aboutUs/', include('aboutUs.urls')),
    path('api/factory/', include('factory.urls')),
    path('api/home/', include('home.urls')),
    path('api/news/', include('news.urls')),
    path('api/products/', include('products.urls')),
    path('api/quality/', include('quality.urls')),
    path('api/reachUs/', include('reachUs.urls')),
    path('api/partnership', include('partnership.urls')),
    path(
        "api/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)