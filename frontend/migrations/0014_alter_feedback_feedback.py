# Generated by Django 5.0.3 on 2024-04-04 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0013_remove_feedback_n_ame_feedback_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
