# Generated by Django 4.2 on 2023-05-08 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='Name', max_length=255),
            preserve_default=False,
        ),
    ]
