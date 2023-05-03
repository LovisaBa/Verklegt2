from django.db import models
from main.models import Products

# Create your models here.


class PizzaTypes(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.type}"


class Pizzas(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.ForeignKey(PizzaTypes, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.CharField(max_length=255, blank=True)
    image = models.CharField(max_length=9999)

    def __str__(self):
        return f"Pizza: {self.name}, ProdId: {self.product_id}"


class PizzaHasType(models.Model):
    pizza = models.ForeignKey(Pizzas, on_delete=models.CASCADE)
    type = models.ForeignKey(PizzaTypes, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pizza: {self.pizza}, Type: {self.type}"


class Ingredients(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.id})"


class PizzaIngredients(models.Model):
    pizza = models.ForeignKey(Pizzas, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pizza: {self.pizza}, Ingredients: {self.ingredient}"


class Drinks(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name}, ProdId: {self.product_id}"
