from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from menu.models import Pizza, Drink
from offers.models import Offer, PizzaOffer, Discount
from offers.views import add_pizzas_to_offer
from .models import *
from main.models import Product
from datetime import datetime

# Create your views here.


def index(request):
    user_order = get_order(request)
    order_items = user_order.items.all()
    for order_item in order_items:
        item = get_item_from_prod_id(order_item.product_id)
        order_item.image = item.image
        order_item.name = item.name
    return render(request, 'orders/index.html', {
        "order_items": order_items,
        "user_order": user_order
    })


def get_item_from_prod_id(prod_id):
    product = Product.objects.get(pk=prod_id)
    if product.type.type == "Pizza":
        return Pizza.objects.get(product_id=prod_id)
    if product.type.type == "Offer":
        off_id = Offer.objects.get(product_id=prod_id)
        return PizzaOffer.objects.get(offer_id=off_id)
    else:
        return Drink.objects.get(product_id=prod_id)


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
        price=get_item_from_prod_id(product_id).price,
        quantity=1
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

def empty_cart(request):
    order = get_order(request)
    order.delete()
    messages.success(request, 'Cart has been emptied')
    return redirect("/orders/")


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
    if new_discount == 50:
        check_50_discount(request, order, day, new_discount)
    if new_discount == 20:
        check_20_discount(request, order, weekday, new_discount)

    return redirect('/offers/')


def add_offer(request, offer_id):
    print('HALLO')
    pizzas = add_pizzas_to_offer(request, offer_id)
    for pizza in pizzas:
        add_to_cart(request, pizza.product_id)

    return redirect('orders_index')
