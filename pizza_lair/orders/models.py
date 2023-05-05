from django.db import models
from main.models import Product
from users.models import User

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f"User: {self.user}"
