from django.db import models

# Create your models here.


class Country(models.Model):
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.country}"


class User(models.Model):
    name = models.CharField(max_length=255)
    phoneNumber = models.IntegerField()
    streetName = models.CharField(max_length=255)
    houseNumber = models.IntegerField()
    zipCode = models.IntegerField()
    city = models.CharField(max_length=255)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg')

    def __str__(self):
        return f"Name: {self.name}, Number: {self.phoneNumber}"


class Payment(models.Model):
    cardHolder = models.CharField(max_length=255)
    cardNr = models.IntegerField()
    expDate = models.DateTimeField()
    cvv = models.IntegerField()

    def __str__(self):
        return f"CardHolder: {self.cardHolder}"
