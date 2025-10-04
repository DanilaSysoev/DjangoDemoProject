from django.shortcuts import render, HttpResponse
from random import choice
from .models import Wish

def index(request):
    wishes = Wish.objects.all()
    select = choice(wishes)
    select.using_count += 1
    select.save()
    
    return HttpResponse(select)
