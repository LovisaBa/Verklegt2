from django.contrib.auth.models import User
from django.db import models
from users.models import Profile
from main.models import Product

# Create your models here.


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.CharField(max_length=9999, blank=True)
    name = models.CharField(max_length=255, blank=True)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.type} {self.quantity} {self.price}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem, blank=True)
    ordered = models.BooleanField(default=False)
    discount = models.PositiveIntegerField(default=0)

    def get_price(self):
        total = 0
        for item in self.items.all():
            total += item.price*item.quantity
        return total

    def get_discount_price(self):
        total = self.get_price()
        return round(total * (1 - (self.discount / 100)))

    def __str__(self):
        return f"{self.id} User: {self.user} Ordered: {self.ordered}"
