from django.db import models
from main.models import Products
from users.models import Users

# Create your models here.


class Orders(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return f"User: {self.user}"


class ProdOrders(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, default="")
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order: {self.order}, Product: {self.product}"
