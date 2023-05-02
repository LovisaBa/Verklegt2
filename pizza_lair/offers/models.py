from django.db import models
from main.models import Products
from menu.models import Pizzas

# Create your models here.
class Offers(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

class Discounts(models.Model):
    offer = models.ForeignKey(Offers, on_delete=models.CASCADE)
    discount = models.FloatField()

class PizzaOffers(models.Model):
    offer = models.ForeignKey(Offers, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()

class PizzasInOffers(models.Model):
    pizzaoffers = models.ForeignKey(PizzaOffers, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizzas, on_delete=models.CASCADE)

