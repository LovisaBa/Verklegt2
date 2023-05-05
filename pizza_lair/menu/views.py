from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404
from menu.models import Pizza

# Create your views here.


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        pizzas = list(Pizza.objects.filter(name__icontains=search_filter).values())
        return JsonResponse({ 'data': pizzas })
    return render(request, 'pizza/index.html', {
        "pizzas": Pizza.objects.all().order_by('name')
    })


def get_pizza_by_id(request, id):
    return render(request, 'pizza/pizza_details.html', {
        'pizza': get_object_or_404(Pizza, pk=id)
    })
