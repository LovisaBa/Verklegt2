from django.shortcuts import render, get_object_or_404
from menu.models import Pizza

# Create your views here.


def index(request):
    return render(request, 'pizza/index.html', {
        "pizzas": Pizza.objects.all()
    })


def get_pizza_by_id(request, id):
    return render(request, 'pizza/pizza_details.html', {
        'pizza': get_object_or_404(Pizza, pk=id)
    })
