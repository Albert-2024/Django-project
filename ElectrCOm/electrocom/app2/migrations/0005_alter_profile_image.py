# Generated by Django 4.2.5 on 2023-10-07 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0004_alter_profile_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='sample/'),
        ),
    ]
