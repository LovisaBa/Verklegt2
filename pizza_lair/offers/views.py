from django.shortcuts import render, get_object_or_404
from menu.models import Pizza
from offers.models import PizzaOffer, Discount


# Create your views here.


def index(request):
    """Renders the site for all offers."""
    return render(request, 'offers/index.html', {
        "offers": PizzaOffer.objects.all(),
        "discounts": Discount.objects.all()
    })


def get_offer(request, offer_id) -> PizzaOffer:
    """Returns a render of a detailed view of each offer
        with all the required information."""
    offer = get_object_or_404(PizzaOffer, pk=offer_id)
    amount = [x for x in range(offer.pizza_amount)]
    return render(request, 'offers/offer_details.html', {
        'offer': offer,
        'amount': amount,
        'pizzas': Pizza.objects.all().order_by('name')
    })


def get_discount(request, offer_id) -> Discount:
    """ Returns a render of a detailed view of a discount.If
        that item is not found it returns a 404 error."""
    return render(request, 'offers/discount_details.html', {
        'discount': get_object_or_404(Discount, pk=offer_id)
    })


def get_offer_by_id(offer_id) -> PizzaOffer:
    """Returns an offer from the offer id. If that item is
        not found it returns a 404 error."""
    return get_object_or_404(PizzaOffer, pk=offer_id)

