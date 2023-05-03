from django.db import models

# Create your models here.


class Products(models.Model):
    product = models.CharField(max_length=255)

    def __str__(self):
        return f"ProductNr: {self.id}"
