from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Pizza, Drink

# Create your views here.


def index(request):
    """Renders the menu site. Includes search and filter methods"""
    if 'pizza_filter' in request.GET:
        data = get_pizzas_by_type(request)
        return JsonResponse({'data': data})
    if 'search_filter' in request.GET:
        data = get_pizzas_by_search(request)
        return JsonResponse({'data': data})
    if 'order_by' in request.GET:
        data = order_pizzas_by(request)
        return JsonResponse({'data': data})
    return render(request, 'pizza/index.html', {
        "pizzas": Pizza.objects.all().order_by('name'),
        "drinks": Drink.objects.all().order_by('name')
    })


def order_pizzas_by(request) -> list:
    """Returns a list all pizzas ordered by price or name."""
    order_by = request.GET['order_by']
    if order_by == 'order_by_price':
        data = list(Pizza.objects.all().values().order_by('price'))
    else:
        data = list(Pizza.objects.all().values().order_by('name'))
    return data


def get_pizzas_by_type(request) -> list:
    """Returns a list of all pizzas filtered by type."""
    pizza_filter = request.GET['pizza_filter']
    return list(Pizza.objects.filter(type__type__icontains=pizza_filter).values())


def get_pizzas_by_search(request) -> list:
    """Returns a list of all pizzas filtered by a search."""
    search_filter = request.GET['search_filter']
    return list(Pizza.objects.filter(name__icontains=search_filter).values())


def get_pizza_by_id(request, product_id) -> Pizza:
    """Returns a Pizza object from product_id"""
    return render(request, 'pizza/pizza_details.html', {
        'pizza': get_object_or_404(Pizza, pk=product_id)
    })


def get_drink_by_id(request, drink_id) -> Drink:
    """Returns a drink from its id"""
    return render(request, 'pizza/drink_details.html', {
        'drink': get_object_or_404(Drink, pk=drink_id)
    })
