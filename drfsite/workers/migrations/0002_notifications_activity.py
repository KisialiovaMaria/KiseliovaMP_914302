# Generated by Django 4.1.2 on 2022-11-17 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='activity',
            field=models.BooleanField(null=True),
        ),
    ]
