# Generated by Django 4.2 on 2023-05-10 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0010_remove_pizzaoffer_pizzas_pizzaoffer_pizza_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzaoffer',
            name='testfield',
            field=models.CharField(default='a', max_length=5),
        ),
        migrations.AlterField(
            model_name='pizzaoffer',
            name='pizza_amount',
            field=models.IntegerField(default=2),
        ),
    ]
