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
    offer = get_object_or_404(PizzaOffer, pk=id)
    amount = [x for x in range(offer.pizza_amount)]
    return render(request, 'offers/offer_details.html', {
        'offer': offer,
        'amount': amount,
        'pizzas': Pizza.objects.all().order_by('name')
    })


def get_discount(request, id) -> Discount:
    return render(request, 'offers/discount_details.html', {
        'discount': get_object_or_404(Discount, pk=id)
    })


def get_offer_by_id(offer_id):
    return get_object_or_404(PizzaOffer, pk=offer_id)

