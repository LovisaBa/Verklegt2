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


def index(request):
    """Returns the main cart page with the information
        about the users order and order items."""
    user_order = get_order(request)
    order_items = user_order.items.all()
    order_items = get_order_images(order_items)
    return render(request, 'orders/index.html', {
        "order_items": order_items,
        "user_order": user_order
    })


def get_item_from_prod_id(prod_id):
    """Returns an item, given its product id."""
    product = Product.objects.get(pk=prod_id)
    if product.type.type == "Pizza":
        return Pizza.objects.get(product_id=prod_id)
    if product.type.type == "Offer":
        off_id = Offer.objects.get(product_id=prod_id)
        return PizzaOffer.objects.get(offer_id=off_id)
    else:
        return Drink.objects.get(product_id=prod_id)


def get_order_images(order_items):
    """Gets images for all order items to be places in the cart"""
    for order_item in order_items:
        item = get_item_from_prod_id(order_item.product_id)
        order_item.image = item.image
        order_item.name = item.name
    return order_items


def get_order(request) -> Order:
    """Returns the order for the logged-in user"""
    user_order = Order.objects.filter(user=request.user, ordered=False)

    if user_order.exists():
        order = user_order[0]
        order.save()
    else:
        order = Order.objects.create(user=request.user)
        order.save()
    return order


def add_to_order(request, order, order_item, pk):
    """Adds an item to an order. If the item already exists in the order,
        the quantity is increased"""
    if order.items.filter(product__pk=pk, price=order_item.price).exists():
        order_item.quantity += 1
    else:
        order.items.add(order_item)
    order_item.save()
    order.save()


def add_to_cart(request, product_id):
    """Adds a product to the current users cart"""
    product = get_object_or_404(Product, pk=product_id)
    price = get_item_from_prod_id(product_id).price
    order_item, created = create_order_item(product, price, 1, False)
    order = get_order(request)
    add_to_order(request, order, order_item, product.pk)
    messages.info(request, "Item added to cart.")
    return redirect('/menu/')


def increase_quantity(request, product_id, price, quantity):
    """Increases the amount of the given product by 1"""
    product = get_object_or_404(Product, pk=product_id)
    order_item, create = create_order_item(product, price, quantity, False)
    order = get_order(request)
    add_to_order(request, order, order_item, product.pk)
    messages.info(request, 'Quantity increased.')
    return redirect('/orders/')


def decrease_quantity(request, order_item_id):
    """Decreased the amount of the given product by 1"""
    order_item = get_object_or_404(OrderItem, pk=order_item_id)
    order = get_order(request)
    remove_from_order(request, order, order_item)
    return redirect('/orders/')


def remove_from_order(request, order, order_item):
    """Removes 1 item from an order. If there is only 1 item to begin with,
        it fully removes the item from the order"""
    if order_item.quantity == 1:
        order.items.remove(order_item)
        messages.info(request, 'Item removed from cart.')
    else:
        order_item.quantity -= 1
        messages.info(request, 'Quantity decreased.')
    order_item.save()
    order.save()


def empty_cart(request):
    """Empties the whole cart."""
    order = get_order(request)
    order.delete()
    messages.success(request, 'Cart has been emptied.')
    return redirect("/orders/")


def check_50_discount(request, order, day, discount):
    """Checks if the 50% discount is valid at the time it's added."""
    if day == 28:
        order.discount = discount
        order.save()
        messages.success(request, 'Discount added!')
    else:
        messages.error(request, 'This discount is only valid on the 28th of the month.')


def check_20_discount(request, order, weekday, discount):
    """Checks if the 20% discount is valid at the time it is added to an order."""
    if weekday == 2:
        order.discount = discount
        order.save()
        messages.success(request, 'Discount added!')
    else:
        messages.error(request, 'This discount is only valid on wednesdays.')


def add_discount(request, discount_id):
    """Adds a discount to the users order."""
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
    """Adds an offer to the users order."""
    order = get_order(request)
    offer = get_offer_by_id(offer_id)
    pizza_price = round(offer.price/offer.pizza_amount)
    if request.method == 'POST':
        add_offer_pizzas(request, order, pizza_price)
    return redirect('orders_index')


def add_offer_pizzas(request, order, pizza_price):
    """Adds each individual pizza of an offer to the cart."""
    data = request.POST.getlist('pizza')
    pizzas = []
    for prod_id in data:
        pizza = get_item_from_prod_id(prod_id)
        pizzas.append(pizza)
    pizza_dict = count_pizzas(pizzas)
    for key in pizza_dict:
        order_item, created = create_order_item(key.product, pizza_price, pizza_dict[key], True)
        add_to_order(request, order, order_item, key.product.pk)
    messages.success(request, 'Offer has been added to your order.')


def count_pizzas(pizzas) -> dict:
    """Counts how many of each pizza is in an offer."""
    pizza_dict = {}
    for pizza in pizzas:
        count = pizzas.count(pizza)
        pizza_dict[pizza] = count
    print(pizza_dict)
    return pizza_dict


def create_order_item(product, price, quantity, deal) -> OrderItem:
    """Returns an order item from the given information.
        It gets the corresponding item, or creates it
        if it doesn't exist."""
    return OrderItem.objects.get_or_create(
                product=product,
                price=price,
                quantity=quantity,
                part_of_offer=deal)


def checkout(request):
    """Renders the first step of the checkout phase"""
    user_order = get_order(request)
    user_profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=user_profile, data=request.POST)
        if form.is_valid():
            save_profile_form(request, form)
            return redirect('payment')
        return render(request, 'orders/checkout.html', {
            'user_order': user_order,
            'form': form
        })
    return render(request, 'orders/checkout.html', {
        'user_order': user_order,
        'form': ProfileForm(instance=user_profile)
    })


def save_profile_form(request, form):
    """Saves the user profile form."""
    user_profile = form.save(commit=False)
    user_profile.user = request.user
    user_profile.save()


def save_payment_form(request, form):
    """Saves the payment form."""
    user_payment = form.save(commit=False)
    user_payment.user = request.user
    user_payment.save()


def payment(request):
    """Renders the second step of the payment process,
        the payment form is displayed here."""
    user_order = get_order(request)
    user_payment = Payment.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = PaymentForm(instance=user_payment, data=request.POST)
        if form.is_valid():
            save_payment_form(request, form)
            return redirect('confirm')
        else:
            return render(request, 'orders/payment.html', {
                'user_order': user_order,
                'form': form
            })
    return render(request, 'orders/payment.html', {
        'user_order': user_order,
        'form': PaymentForm(instance=user_payment)
    })


def confirm(request):
    """Renders the read only confirmation step of the checkout process."""
    user_profile = Profile.objects.filter(user=request.user).first()
    user_payment = Payment.objects.filter(user=request.user).first()
    user_order = get_order(request)
    order_items = user_order.items.all()
    order_items = get_order_images(order_items)
    return render(request, 'orders/confirm.html', {
        'user_order': user_order,
        'order_items': order_items,
        'user': user_profile,
        'payment': user_payment
    })


def place_order(request):
    """Changes the users orders status to True and redirects to the main page."""
    order = get_order(request)
    order.ordered = True
    order.save()
    messages.success(request, "Thank you for ordering from REYK. "
                              "You will receive a text when your pizzas "
                              "are placed in the oven. Have a great day :)")
    return redirect('/')
