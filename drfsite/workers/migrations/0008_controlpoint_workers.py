# Generated by Django 4.1.2 on 2022-12-12 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0007_alter_worker_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='controlpoint',
            name='workers',
            field=models.ManyToManyField(through='workers.ControlList', to='workers.worker'),
        ),
    ]
