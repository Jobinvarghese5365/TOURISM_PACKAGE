# Generated by Django 5.0.3 on 2024-04-04 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0011_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='name',
            new_name='N_ame',
        ),
    ]