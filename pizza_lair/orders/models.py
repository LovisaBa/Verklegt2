from django.db import models
from main.models import Products
from users.models import Users

# Create your models here.

class Orders(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    price = models.IntegerField()

class ProdOrders(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)



