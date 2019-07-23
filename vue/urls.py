from django.urls import path, include
from django.contrib import admin

from vue import user_controller

urlpatterns = [
    path('index/', user_controller.index),
    path('list/', user_controller.list),
    path('get/', user_controller.get),
    path('delete/', user_controller.delete),
    path('update/', user_controller.update),
]
