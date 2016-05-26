from django.http import HttpResponse, Http404
from django.shortcuts import render

def index(request):
    context = {
        'name' : 'Edgar Grepo',
        'hobby' : 'Football',
        'language' : 'Python'
    }
    return render(request, 'home/index.html', context)


# Create your views here.
