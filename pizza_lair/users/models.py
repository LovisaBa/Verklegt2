from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Country(models.Model):
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.country}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phoneNumber = models.PositiveIntegerField(validators=[
        MaxValueValidator(9999999, "The Phone number cannot be longer than 7 characters"),
        MinValueValidator(1000000, "The Phone number must be at least 7 characters long")]
    )
    streetName = models.CharField(max_length=255)
    houseNumber = models.PositiveIntegerField()
    zipCode = models.PositiveIntegerField()
    city = models.CharField(max_length=255)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    image = models.CharField(max_length=9999, default='https://t4.ftcdn.net/jpg/04/10/43/77/360_F_410437733_hdq4Q3QOH9uwh0mcqAhRFzOKfrCR24Ta.jpg')

    def __str__(self):
        return f"Name: {self.user.username}, Number: {self.phoneNumber}"


class Payment(models.Model):
    cardHolder = models.CharField(max_length=255)
    cardNr = models.PositiveIntegerField()
    expDate = models.DateTimeField()
    cvv = models.PositiveIntegerField()

    def __str__(self):
        return f"CardHolder: {self.cardHolder}"
