# Generated by Django 4.2 on 2023-05-09 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0007_offer_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzaoffer',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]