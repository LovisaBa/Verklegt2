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

    def __str__(self):
        return f"Name: {self.name}, Number: {self.phoneNumber}"


class Payments(models.Model):
    cardHolder = models.CharField(max_length=255)
    cardNr = models.IntegerField()
    expDate = models.DateTimeField()
    cvv = models.IntegerField()

    def __str__(self):
        return f"CardHolder: {self.cardHolder}"


class UserPayment(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payments, on_delete=models.CASCADE)

    def __str__(self):
        return f"User: {self.user.name}, paymentId: {self.payment_id}"
