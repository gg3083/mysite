from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('list/', views.list),
    # path('del/', views.delete),
]
