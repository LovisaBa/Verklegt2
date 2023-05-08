from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import *
from main.models import Product

# Create your views here.


def index(request):
    return render(request, 'orders/index.html')

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk = pk)
    order_item, created = OrderItem.objects.get_or_create(
        product=product,
        user = request.user,
        ordered = False
    )
    fetched_order = Order.objects.filter(user=request.user, ordered= False)

    if fetched_order.exists():
        order = fetched_order[0]

        if order.product.filter(product__pk = product.pk).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Quantity increased")
            return redirect('menu/')
        else:
            order.items.add(order_item)
            messages.info(request, "Item added")
            return redirect('menu/')
    else:
        order = Order.objects.create(user=request.user)
        order.items.add(order_item)
        messages.info(request, "Item added")
        return redirect('menu/')