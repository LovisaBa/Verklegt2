from django.shortcuts import render, get_object_or_404
from offers.models import PizzaOffer, Discount

# Create your views here.


def index(request):
    return render(request, 'offers/index.html', {
        "offers": PizzaOffer.objects.all(),
        "discounts": Discount.objects.all()
    })


def get_offer_by_id(request, id):
    return render(request, 'offers/offer_details.html', {
        'offer': get_object_or_404(PizzaOffer, pk=id)
    })


def get_discount_by_id(request, id):
    return render(request, 'offers/discount_details.html', {
        'discount': get_object_or_404(Discount, pk=id)
    })
