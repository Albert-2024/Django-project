# Generated by Django 4.2.5 on 2023-09-29 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='subtotal',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='total',
        ),
    ]
