from django.db import models

# Create your models here.

"""class PizzaType(models.Model):
    name = models.CharField(max_length=255)
class Pizza(models.Model):
    # add relevant attributes for pizzas.
    name = models.CharField(max_length=255)
    type = models.ForeignKey(PizzaType, on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.CharField(max_length=255, blank=True)
    toppings = models #??

class PizzaImage(models.Model):
    menu = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    image = models.CharField(max_length=9999)"""
