from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from first_project import settings
from products import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("products.urls")),
]

if settings.DEBUG:  # Only serve media files in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)