# Generated by Django 5.0.3 on 2024-04-04 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0010_user_details_hotel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('feedback', models.TextField()),
            ],
        ),
    ]
