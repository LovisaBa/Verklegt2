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
    price = models.PositiveIntegerField()
    image = models.ImageField(null=True)
    description = models.CharField(max_length=255, blank=True)
    type = models.ManyToManyField(PizzaType)
    ingredient = models.ManyToManyField(Ingredient)

    def __str__(self):
        return f"Pizza: {self.name}, ProdId: {self.product_id}"


class Drink(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}, ProdId: {self.product_id}"


class PizzaImage(models.Model):
    image = models.ImageField(null=True)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)


class DrinkImage(models.Model):
    image = models.ImageField(null=True)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
