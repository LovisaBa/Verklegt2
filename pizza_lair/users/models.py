from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=255)
    phoneNumber = models.IntegerField()
    streetName = models.CharField(max_length=255)
    houseNumber = models.IntegerField()
    zipCode = models.IntegerField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    image = models.CharField(max_length=9999)

class Payments(models.Model):
    cardHolder = models.CharField(max_length=255)
    cardNr = models.IntegerField()
    expDate = models.DateTimeField()
    cvv = models.IntegerField()

class UserPayment(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payments, on_delete=models.CASCADE)
