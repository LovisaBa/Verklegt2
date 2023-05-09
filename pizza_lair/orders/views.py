from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from menu.models import Pizza, Drink
from offers.models import Offer, PizzaOffer, Discount
from .models import *
from main.models import Product

# Create your views here.


def index(request):
    return render(request, 'orders/index.html')


def get_product_price(prod_id):
    product = Product.objects.get(pk=prod_id)
    if product.type.type == "Pizza":
        return Pizza.objects.get(product_id=prod_id).price
    if product.type.type == "Offer":
        off_id = Offer.objects.get(product_id=prod_id)
        return PizzaOffer.objects.get(offer_id=off_id).price
    else:
        return Drink.objects.get(product_id=prod_id).price


def get_order(request):
    user_order = Order.objects.filter(user=request.user, ordered=False)

    if user_order.exists():
        return user_order[0]
    else:
        order = Order.objects.create(user=request.user)
        # TODO HELP
        order.items.clear()
        order.save()
        return order


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    order_item, created = OrderItem.objects.get_or_create(
        product=product,
        price=get_product_price(product_id),
    )
    order = get_order(request)

    if order.items.filter(product__pk=product.pk).exists():
        order_item.quantity += 1
        order_item.save()
        messages.info(request, "Quantity increased")
    else:
        order.items.add(order_item)
        messages.info(request, "Item added")
    return redirect('/menu/')


def add_discount(request, discount_id):
    new_discount = get_object_or_404(Discount, pk=discount_id)
    order = get_order(request)
    order.discount = new_discount.discount
    order.save()

    return redirect('/offers/')
