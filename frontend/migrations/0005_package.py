# Generated by Django 5.0.3 on 2024-03-18 10:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_destination'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spot', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('duration', models.CharField(blank=True, max_length=50, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='package_images')),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('destination', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontend.destination')),
            ],
        ),
    ]