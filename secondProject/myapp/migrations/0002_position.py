# Generated by Django 5.0.1 on 2024-02-19 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('positon', models.CharField(max_length=100)),
                ('salary', models.FloatField()),
            ],
        ),
    ]
