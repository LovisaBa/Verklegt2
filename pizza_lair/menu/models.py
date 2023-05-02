from django.db import models
from main.models import Products

# Create your models here.

class PizzaTypes(models.Model):
    type = models.CharField(max_length=255)

class Pizzas(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.ForeignKey(PizzaTypes, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.CharField(max_length=255, blank=True)
    image = models.CharField(max_length=9999)

class PizzaHasType(models.Model):
    pizza = models.ForeignKey(Pizzas, on_delete=models.CASCADE)
    type = models.ForeignKey(PizzaTypes, on_delete=models.CASCADE)

class Ingredients(models.Model):
    name = models.CharField(max_length=255)

class PizzaIngredients(models.Model):
    pizza = models.ForeignKey(Pizzas, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)



