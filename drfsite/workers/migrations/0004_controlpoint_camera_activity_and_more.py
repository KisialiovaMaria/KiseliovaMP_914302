# Generated by Django 4.1.2 on 2022-12-10 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0003_alter_user_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='controlpoint',
            name='camera_activity',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='controlpoint',
            name='camera_name',
            field=models.CharField(default='fff', max_length=20),
        ),
    ]