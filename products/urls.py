from django.contrib import admin
from django.urls import path

from products import views

urlpatterns = [
    path("", views.index),
    path("create/", views.create),
    path("edit/<int:id>", views.edit),
    path("details/<int:id>", views.details),
    path("delete/<int:id>", views.delete),
]
