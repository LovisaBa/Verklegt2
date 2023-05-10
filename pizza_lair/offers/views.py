from django.shortcuts import render, get_object_or_404

from menu.models import Pizza
from offers.models import PizzaOffer, Discount


# Create your views here.


def index(request):
    return render(request, 'offers/index.html', {
        "offers": PizzaOffer.objects.all(),
        "discounts": Discount.objects.all()
    })


def get_offer(request, id) -> PizzaOffer:
    print(request.POST)
    return render(request, 'offers/offer_details.html', {
        'offer': get_object_or_404(PizzaOffer, pk=id),
        #"pizzas"
    })


def get_discount(request, id) -> Discount:
    return render(request, 'offers/discount_details.html', {
        'discount': get_object_or_404(Discount, pk=id)
    })


def get_offer_by_id(offer_id):
    return get_object_or_404(PizzaOffer, pk=offer_id)


def get_pizzas(request, amount):
    pizzas = []
    return pizzas


def add_pizzas_to_offer(request, offer_id):
    offer = get_offer_by_id(offer_id)
    amount = offer.pizza_amount
    pizzas = get_pizzas(request, amount)
    for pizza in pizzas:
        pizza.price = round(offer.price/offer.pizza_amount)
    return pizzas
