# Generated by Django 4.2 on 2023-05-08 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0007_offer_type'),
        ('menu', '0003_rename_drinks_drink'),
        ('orders', '0003_order_payed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AddField(
            model_name='order',
            name='dicount',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='order',
            name='offer',
            field=models.ManyToManyField(blank=True, to='offers.pizzaoffer'),
        ),
        migrations.AddField(
            model_name='order',
            name='pizza',
            field=models.ManyToManyField(blank=True, to='menu.pizza'),
        ),
    ]