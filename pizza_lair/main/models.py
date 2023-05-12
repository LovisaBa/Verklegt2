from django.db import models


class ProdType(models.Model):
    type = models.TextField(max_length=255)

    def __str__(self):
        return f"{self.type}"


class Product(models.Model):
    type = models.ForeignKey(ProdType, on_delete=models.CASCADE)

    def __str__(self):
        return f"ProductNr: {self.id}"
