# Generated by Django 5.0.1 on 2024-08-22 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_orderproduct_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='total_price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
