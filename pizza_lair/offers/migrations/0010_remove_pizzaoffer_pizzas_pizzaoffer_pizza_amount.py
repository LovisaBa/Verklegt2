# Generated by Django 4.2 on 2023-05-10 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0009_alter_discount_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizzaoffer',
            name='pizzas',
        ),
        migrations.AddField(
            model_name='pizzaoffer',
            name='pizza_amount',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
