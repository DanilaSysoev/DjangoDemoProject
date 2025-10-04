from django.contrib import admin
from django.urls import path, include

from random_wish.views import index


urlpatterns = [
    path('', name='index', view=index),
]