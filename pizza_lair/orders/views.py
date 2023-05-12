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
    if order.items.filter(product__pk=pk, price=order_item.price).exists():
        order_item.quantity += 1
    else:
        order.items.add(order_item)
    order_item.save()
    order.save()


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    price = get_item_from_prod_id(product_id).price
    order_item, created = create_order_item(product, price, 1, False)
    order = get_order(request)
    add_to_order(request, order, order_item, product.pk)
    messages.info(request, "Item added")
    return redirect('/menu/')


def increase_quantity(request, product_id, price, quantity):
    product = get_object_or_404(Product, pk=product_id)
    order_item, create = create_order_item(product, price, quantity, False)
    order = get_order(request)
    add_to_order(request, order, order_item, product.pk)
    messages.info(request, 'Quantity increased')
    return redirect('/orders/')


def decrease_quantity(request, order_item_id, product_id):
    product = get_object_or_404(Product, pk=product_id)
    order_item = get_object_or_404(OrderItem, pk=order_item_id)
    order = get_order(request)
    remove_from_order(request, order, order_item, product.pk)
    return redirect('/orders/')


def remove_from_order(request, order, order_item, pk):
    if order_item.quantity == 1:
        order.items.remove(order_item)
        messages.info(request, 'Item removed')
    else:
        order_item.quantity -= 1
        messages.info(request, 'Quantity decreased')
    order_item.save()
    order.save()


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
            pizza = get_item_from_prod_id(prod_id)
            pizzas.append(pizza)
        pizza_dict = count_pizzas(pizzas)
        for key in pizza_dict:
            order_item, created = create_order_item(key.product, pizza_price, pizza_dict[key], True)
            add_to_order(request, order, order_item, key.product.pk)
        messages.success(request, 'Offer has been added to your order')
    return redirect('orders_index')


def count_pizzas(pizzas) -> dict:
    pizza_dict = {}
    for pizza in pizzas:
        count = pizzas.count(pizza)
        pizza_dict[pizza] = count
    print(pizza_dict)
    return pizza_dict


def create_order_item(product, price, quantity, deal):
    return OrderItem.objects.get_or_create(
                product=product,
                price=price,
                quantity=quantity,
                part_of_offer=deal)


def checkout(request):
    user_order = get_order(request)
    user_profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=user_profile, data=request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            messages.success(request, 'User was successfully updated!')
            return redirect('payment')
        else:
            phone_number_errors = form.errors.get('phoneNumber')
            if phone_number_errors:
                messages.error(request, phone_number_errors[0])
            else:
                messages.error(request, 'There was an error updating the user.')
        return redirect('checkout')
    return render(request, 'orders/checkout.html', {
        'user_order': user_order,
        'form': ProfileForm(instance=user_profile)
    })


def payment(request):
    user_order = get_order(request)
    user_profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = PaymentForm(instance=user_profile, data=request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            messages.success(request, 'Payment information was successfully updated!')
            return redirect('confirm')
        else:
            card_number_errors = form.errors.get('cardNumber')
            if card_number_errors:
                messages.error(request, card_number_errors[0])
            else:
                messages.error(request, 'There was an error updating payment details.')
        return redirect('payment')
    return render(request, 'orders/payment.html', {
        'user_order': user_order,
        'form': PaymentForm(instance=user_profile)
    })


def confirm(request):
    user_profile = Profile.objects.filter(user=request.user).first()
    user_payment = Payment.objects.filter(user=request.user).first()
    user_order = get_order(request)
    order_items = user_order.items.all()
    return render(request, 'orders/confirm.html', {
        'user_order': user_order,
        'order_items': order_items,
        'user': user_profile,
        'payment': user_payment
    })


def place_order(request):
    order = get_order(request)
    order.ordered = True
    order.save()
    messages.success(request, "Thank you for ordering from REYK. "
                              "You will receive a text when your pizzas "
                              "are placed in the oven. Have a great day :)")
    return redirect('/')
