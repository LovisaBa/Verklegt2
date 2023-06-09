# Generated by Django 4.2 on 2023-05-09 13:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_payment_cardnr_alter_payment_cvv_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phoneNumber',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999, 'The Phone number cannot be longer than 7 characters'), django.core.validators.MinValueValidator(1000000, 'The Phone number must be at least 7 characters long')]),
        ),
    ]
