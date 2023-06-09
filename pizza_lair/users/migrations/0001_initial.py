# Generated by Django 4.2 on 2023-05-04 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardHolder', models.CharField(max_length=255)),
                ('cardNr', models.IntegerField()),
                ('expDate', models.DateTimeField()),
                ('cvv', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phoneNumber', models.IntegerField()),
                ('streetName', models.CharField(max_length=255)),
                ('houseNumber', models.IntegerField()),
                ('zipCode', models.IntegerField()),
                ('city', models.CharField(max_length=255)),
                ('image', models.ImageField(default='default.jpg', upload_to='')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.country')),
            ],
        ),
    ]
