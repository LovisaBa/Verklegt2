from django.db import models
from main.models import Products
from menu.models import Pizzas

# Create your models here.


class Offers(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return f"OffId: {self.id}, ProdId: {self.product_id}"


class Discounts(models.Model):
    offer = models.ForeignKey(Offers, on_delete=models.CASCADE)
    discount = models.FloatField()

    def __str__(self):
        return f"OffId: {self.offer_id}, Discount:{self.discount}"


class PizzaOffers(models.Model):
    offer = models.ForeignKey(Offers, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return f"OffId: {self.offer_id}, Name: {self.name}"


class PizzasInOffers(models.Model):
    pizzaOffer = models.ForeignKey(PizzaOffers, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizzas, on_delete=models.CASCADE)

    def __str__(self):
        return f"OffId: {self.pizzaOffer}, pizza: {self.pizza}"

