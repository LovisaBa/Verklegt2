# Generated by Django 4.2 on 2023-05-09 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='cardNr',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='cvv',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='houseNumber',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phoneNumber',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='zipCode',
            field=models.PositiveIntegerField(),
        ),
    ]
