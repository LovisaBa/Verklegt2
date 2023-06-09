from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField

TODAY = datetime.now()
YEAR = int(TODAY.strftime('%y'))
EXP_YEAR = int(YEAR) + 10


class Country(models.Model):
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.country}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phoneNumber = models.PositiveIntegerField(validators=[
        MaxValueValidator(9999999, message="The Phone number cannot be longer than 7 characters"),
        MinValueValidator(1000000, message="The Phone number must be at least 7 characters long")]
    )
    streetName = models.CharField(max_length=255)
    houseNumber = models.PositiveIntegerField()
    zipCode = models.PositiveIntegerField()
    city = models.CharField(max_length=255)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    image = models.CharField(max_length=9999, default='https://t4.ftcdn.net/jpg/04/10/43/77'
                                                      '/360_F_410437733_hdq4Q3QOH9uwh0mcqAhRFzOKfrCR24Ta.jpg')

    def __str__(self):
        return f"Name: {self.user.username}, Number: {self.phoneNumber}"


class Payment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    cardHolder = models.CharField('card holder', max_length=255)
    cardNumber = CardNumberField('card number', null=True)
    expDate = CardExpiryField('expiration date', null=True)
    cvvCode = SecurityCodeField('security code', null=True)

    def __str__(self):
        return f"CardHolder: {self.cardHolder}"
