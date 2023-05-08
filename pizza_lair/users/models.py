from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Country(models.Model):
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.country}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.IntegerField()
    streetName = models.CharField(max_length=255)
    houseNumber = models.IntegerField()
    zipCode = models.IntegerField()
    city = models.CharField(max_length=255)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    image = models.CharField(max_length=9999, default='http://127.0.0.1:8000/media/default.jpg')

    def __str__(self):
        return f"Name: {self.user.username}, Number: {self.phoneNumber}"


class Payment(models.Model):
    cardHolder = models.CharField(max_length=255)
    cardNr = models.IntegerField()
    expDate = models.DateTimeField()
    cvv = models.IntegerField()

    def __str__(self):
        return f"CardHolder: {self.cardHolder}"
