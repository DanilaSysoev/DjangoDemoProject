from django.shortcuts import render
from random import choice
from .models import Wish

def index(request):
    wishes = Wish.objects.all()
    select = choice(wishes)
    select.using_count += 1
    select.save()
    
    context = {
        'title': 'Random wish',
        'value': select
    }
    
    return render(request, 'index.html', context)


def all_wishes(request):
    wishes = Wish.objects.all()
    context = {
        'wishes': wishes
    }
    return render(request, 'all.html', context)
    