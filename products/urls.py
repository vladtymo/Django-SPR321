from django.contrib import admin
from django.urls import path

from products import views

urlpatterns = [
    path("", views.index),
    path("details/<int:id>", views.details),
    path("delete/<int:id>", views.delete),
]
