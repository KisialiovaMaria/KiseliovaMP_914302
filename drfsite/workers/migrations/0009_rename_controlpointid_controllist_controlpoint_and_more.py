# Generated by Django 4.1.2 on 2022-12-12 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0008_controlpoint_workers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='controllist',
            old_name='controlPointID',
            new_name='controlPoint',
        ),
        migrations.RenameField(
            model_name='controllist',
            old_name='workerID',
            new_name='worker',
        ),
    ]