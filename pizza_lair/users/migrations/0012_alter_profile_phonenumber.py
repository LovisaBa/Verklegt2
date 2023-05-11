# Generated by Django 4.2 on 2023-05-11 15:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_profile_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phoneNumber',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999, message='The Phone number cannot be longer than 7 characters'), django.core.validators.MinValueValidator(1000000, message='The Phone number must be at least 7 characters long')]),
        ),
    ]
