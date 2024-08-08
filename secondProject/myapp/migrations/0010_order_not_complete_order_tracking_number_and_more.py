# Generated by Django 5.0.1 on 2024-08-05 13:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_product_introduction'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='not_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='tracking_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='TrackingOrderID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=10)),
                ('tracking_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_id', to='myapp.order')),
            ],
        ),
    ]