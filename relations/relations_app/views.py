from django.shortcuts import render
from relations_app.models import Human, City, Course, Student

def index(request):
    context = {
        'humans': Human.objects.all(),
        'cities': City.objects.all(),
    }
    return render(request, template_name='index.html', context=context)

def courses(request):
    context = {
        'courses': Course.objects.all(),
        'students': Student.objects.all(),
    }
    return render(request, template_name='courses.html', context=context)

def human(request, id: int):
    context = {
        'human': Human.objects.get(id=id),
    }
    return render(request, template_name='human.html', context=context)
