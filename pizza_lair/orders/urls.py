from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/pizzas
    path('', views.index, name="orders_index"),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add_discount/<int:discount_id>/', views.add_discount, name='add_discount'),
    path('add_offer/<int:offer_id>/', views.add_offer, name='add_offer'),
    path('empty_cart/', views.empty_cart, name='empty_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.payment, name='payment'),
    path('confirm/', views.confirm, name='confirm'),
    path('increase_quantity/<int:order_item_id>/<int:product_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:order_item_id>/<int:product_id>/', views.decrease_quantity, name='decrease_quantity')
]
