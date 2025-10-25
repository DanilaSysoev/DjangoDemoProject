from django.urls import path
from relations_app.views import index, courses

urlpatterns = [
    path('', view=index, name='index_empty'),
    path('index/', view=index, name='index'),
    path('courses/', view=courses, name='courses'),
]
