# Generated by Django 4.2 on 2023-05-11 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_remove_payment_expdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='ExpMont',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='expDate',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
