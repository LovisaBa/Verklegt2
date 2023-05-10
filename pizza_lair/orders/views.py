from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from menu.models import Pizza, Drink
from offers.models import Offer, PizzaOffer, Discount
from .models import *
from main.models import Product
from datetime import datetime
from offers.views import get_offer_by_id
from users.forms.user_form import ProfileForm, PaymentForm
from users.models import Profile, Payment

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


def add_to_order(request, order, order_item, pk):
    if order.items.filter(product__pk=pk).exists():
        order_item.quantity += 1
    else:
        order.items.add(order_item)
    order_item.save()
    order.save()


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    price = get_item_from_prod_id(product_id).price
    order_item, created = create_order_item(product, price)
    order = get_order(request)
    add_to_order(request, order, order_item, product.pk)
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
    order = get_order(request)
    offer = get_offer_by_id(offer_id)
    pizza_price = round(offer.price/offer.pizza_amount)
    if request.method == 'POST':
        data = request.POST.getlist('pizza')
        pizzas = []
        for prod_id in data:
            pizzas.append(get_item_from_prod_id(prod_id))
        for pizza in pizzas:
            order_item, created = create_order_item(pizza.product, pizza_price)
            add_to_order(request, order, order_item, pizza.product.pk)
    messages.success(request, 'Offer has been added to your order')
    return redirect('orders_index')


def create_order_item(product, price):
    return OrderItem.objects.get_or_create(
                product=product,
                price=price,
                quantity=1)


def checkout(request):
    user_profile = Profile.objects.filter(user=request.user).first()
    return render(request, 'orders/checkout.html', {
        'form': ProfileForm(instance=user_profile)
    })

