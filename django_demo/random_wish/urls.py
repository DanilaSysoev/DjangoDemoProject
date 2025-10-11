from django.contrib import admin
from django.urls import path, include

from random_wish.views import index, all_wishes


urlpatterns = [
    path('', name='index', view=index),
    path('all/', name='all', view=all_wishes),
]