# Generated by Django 4.2 on 2023-05-08 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_type'),
        ('orders', '0004_remove_order_products_order_dicount_order_offer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='payed',
            new_name='ordered',
        ),
        migrations.RemoveField(
            model_name='order',
            name='dicount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='offer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pizza',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='orders.orderitem'),
        ),
    ]
