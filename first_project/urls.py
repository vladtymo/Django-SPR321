from django.contrib import admin
from django.urls import path

from products import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", views.index),
    path("details/", views.details),
]
