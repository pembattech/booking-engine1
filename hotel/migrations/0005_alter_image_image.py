# Generated by Django 5.0 on 2023-12-22 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_image_remove_hotel_image_alter_hotel_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='hotel/hotel_images/'),
        ),
    ]