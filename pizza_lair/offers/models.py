from django.db import models
from main.models import Product
from menu.models import Pizza

# Create your models here.


class Offer(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"OffId: {self.id}, ProdId: {self.product_id}"


class Discount(models.Model):
    offer = models.OneToOneField(Offer, on_delete=models.CASCADE)
    discount = models.FloatField()

    def __str__(self):
        return f"OffId: {self.offer_id}, Discount:{self.discount}"


class PizzaOffer(models.Model):
    offer = models.OneToOneField(Offer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    pizzas = models.ManyToManyField(Pizza)

    def __str__(self):
        return f"OffId: {self.offer_id}, Name: {self.name}"
