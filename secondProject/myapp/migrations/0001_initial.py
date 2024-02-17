# Generated by Django 5.0.1 on 2024-02-16 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=100)),
                ('tracking', models.CharField(blank=True, max_length=100, null=True)),
                ('other', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
