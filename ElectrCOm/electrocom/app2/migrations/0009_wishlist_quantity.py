# Generated by Django 4.2.5 on 2023-10-12 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0008_alter_sellerprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
