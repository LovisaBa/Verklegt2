from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/pizzas
    path('', views.index, name="pizza_index"),
]