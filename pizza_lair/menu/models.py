from django.db import models
from main.models import Product

# Create your models here.


class PizzaType(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.type}"


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.id})"


class Pizza(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField()
    type = models.ManyToManyField(PizzaType)
    ingredient = models.ManyToManyField(Ingredient)

    def __str__(self):
        return f"Pizza: {self.name}, ProdId: {self.product_id}"


class Drink(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return f"{self.name}, ProdId: {self.product_id}"
