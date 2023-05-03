from django.shortcuts import render
from menu.models import *

# Create your views here.


def index(request):
    return render(request, 'pizza/index.html', {
        "ingredients": Ingredients.objects.all()
    })

