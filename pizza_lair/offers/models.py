from django.db import models
from main.models import Product
from menu.models import Pizza

# Create your models here.


class OffType(models.Model):
    type = models.TextField(max_length=255)

    def __str__(self):
        return f"{self.type}"


class Offer(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    type = models.ForeignKey(OffType, on_delete=models.CASCADE)

    def __str__(self):
        return f"OffId: {self.id}, ProdId: {self.product_id}"


class Discount(models.Model):
    offer = models.OneToOneField(Offer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    discount = models.PositiveIntegerField()
    image = models.ImageField()

    def __str__(self):
        return f"OffId: {self.offer_id}, Discount:{self.discount}"


class PizzaOffer(models.Model):
    offer = models.OneToOneField(Offer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    pizza_amount = models.IntegerField(default=2)
    image = models.ImageField()

    def __str__(self):
        return f"OffId: {self.offer_id}, Name: {self.name}"
