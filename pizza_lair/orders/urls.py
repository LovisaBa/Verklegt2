from django.urls import path
from . import views
from .views import add_to_cart

urlpatterns = [
    # http://localhost:8000/pizzas
    path('', views.index, name="orders_index"),
    path('add-to-cart/<int:id>/', add_to_cart, name='add_to_cart')
]
