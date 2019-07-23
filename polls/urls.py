from django.urls import path, include
from django.contrib import admin

from . import bizhi
from . import views

urlpatterns = [
    path('list/', views.list),
    path('index/',bizhi.list),
    path('add/',bizhi.addPage),
    path('upload/',bizhi.add)
    # path('del/', views.delete),
]
