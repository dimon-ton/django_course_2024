# Generated by Django 5.0.1 on 2024-07-10 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_product_price_product_normal_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='introduction',
            field=models.TextField(blank=True, null=True),
        ),
    ]