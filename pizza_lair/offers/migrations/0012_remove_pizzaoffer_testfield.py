# Generated by Django 4.2 on 2023-05-10 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0011_pizzaoffer_testfield_alter_pizzaoffer_pizza_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizzaoffer',
            name='testfield',
        ),
    ]
