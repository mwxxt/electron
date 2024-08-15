# Generated by Django 5.1 on 2024-08-15 11:23

import django.contrib.auth.models
import django.db.models.deletion
import django.db.models.manager
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('user.user',),
            managers=[
                ('employee', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='employeeprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee_profile', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
