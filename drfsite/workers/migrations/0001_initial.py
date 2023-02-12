# Generated by Django 4.1.2 on 2022-11-16 19:08

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ControlPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departmentName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventType', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positionName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rolename', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SendType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sendType', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='VisitType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitTypeName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=25)),
                ('patronymic', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=25)),
                ('departmentID', models.ForeignKey(on_delete=django.db.models.fields.NOT_PROVIDED, to='workers.department')),
                ('positionID', models.ForeignKey(on_delete=django.db.models.fields.NOT_PROVIDED, to='workers.position')),
            ],
        ),
        migrations.CreateModel(
            name='VisitJuornal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('controlPointID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workers.controlpoint')),
                ('fixedPhotoID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workers.photobase')),
                ('personID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workers.worker')),
                ('visitTypeID', models.ForeignKey(on_delete=django.db.models.fields.NOT_PROVIDED, to='workers.visittype')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('activity', models.CharField(choices=[('1', 'Администратор'), ('2', 'Пользователь')], default='1', max_length=1)),
                ('roleID', models.ForeignKey(on_delete=django.db.models.fields.NOT_PROVIDED, to='workers.role')),
                ('workerID', models.ForeignKey(on_delete=django.db.models.fields.NOT_PROVIDED, to='workers.worker')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('periodFrom', models.DateField()),
                ('periodTo', models.DateField()),
                ('text', models.CharField(max_length=400)),
                ('authID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workers.user')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('workerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workers.worker')),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventTypeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workers.eventtype')),
                ('sendTypeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workers.sendtype')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workers.user')),
            ],
        ),
        migrations.CreateModel(
            name='ControlList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('controlPointID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workers.controlpoint')),
                ('workerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workers.worker')),
            ],
        ),
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipAdress', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=20)),
                ('controlPointID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='workers.controlpoint')),
            ],
        ),
    ]
