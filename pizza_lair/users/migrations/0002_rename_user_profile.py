# Generated by Django 4.2 on 2023-05-05 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_products'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Profile',
        ),
    ]
