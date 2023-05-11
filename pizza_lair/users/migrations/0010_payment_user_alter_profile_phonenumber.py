# Generated by Django 4.2 on 2023-05-11 09:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0009_alter_profile_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phoneNumber',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999, 'The Phone number cannot be longer than 7 characters'), django.core.validators.MinValueValidator(1000000, 'The Phone number must be at least 7 characters long')]),
        ),
    ]
