from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from menu.models import Pizza, Drink
from offers.models import Offer, PizzaOffer, Discount
from .models import *
from main.models import Product
from datetime import datetime

# Create your views here.


def index(request):
    user_order = Order.objects.filter(user=request.user, ordered=False)
    order_items = user_order[0].items.all()
    items = []
    for item in order_items:
        if item.product.type.type == "Pizza":
            prod_id = item.product.id
            pizza = Pizza.objects.get(product_id=prod_id)
            items.append(pizza)
        elif item.product.type.type == "Offer":
            prod_id = item.product.id
            off_id = Offer.objects.get(product_id=prod_id)
            offer = PizzaOffer.objects.get(offer_id=off_id)
            items.append(offer)
        else:
            prod_id = item.product.id
            drink = Drink.objects.get(product_id=prod_id)
            items.append(drink)
    return render(request, 'orders/index.html', {
        "items": items,
        "order_items": order_items
    })


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
        order = user_order[0]
        order.save()
    else:
        order = Order.objects.create(user=request.user)
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
        order.save()
        messages.info(request, "Quantity increased")
    else:
        order.items.add(order_item)
        order.save()
        print(order.items.all())
        messages.info(request, "Item added")
    return redirect('/menu/')


def check_50_discount(request, order, day, discount):
    if day == 28:
        order.discount = discount
        order.save()
        messages.success(request, 'Discount added!')
    else:
        messages.error(request, 'This discount is only valid on the 28th of the month.')


def check_20_discount(request, order, weekday, discount):
    if weekday == 2:
        order.discount = discount
        order.save()
        messages.success(request, 'Discount added!')
    else:
        messages.error(request, 'This discount is only valid on wednesdays.')


def add_discount(request, discount_id):
    today = datetime.now()
    weekday = today.weekday()
    day = today.strftime("%b")
    new_discount = get_object_or_404(Discount, pk=discount_id).discount
    order = get_order(request)
    if new_discount == 0.5:
        check_50_discount(request, order, day, new_discount)
    if new_discount == 0.2:
        check_20_discount(request, order, weekday, new_discount)

    return redirect('/offers/')
