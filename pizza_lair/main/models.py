from django.db import models

# Create your models here.


class Product(models.Model):
    def __str__(self):
        return f"ProductNr: {self.id}"
