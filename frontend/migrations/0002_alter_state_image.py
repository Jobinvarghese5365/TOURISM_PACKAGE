# Generated by Django 4.2.6 on 2024-03-13 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='state_images/'),
        ),
    ]
