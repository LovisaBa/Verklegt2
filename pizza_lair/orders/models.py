from django.db import models
from users.models import Profile
from main.models import Product

# Create your models here.


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product.type} {self.quantity} {self.price}"


class Order(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)

    def get_price(self):
        total = 0
        for item in self.items.all():
            total += item.price
        return total

    def __str__(self):
        return f"User: {self.user}"
