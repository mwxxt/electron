# Generated by Django 5.0 on 2024-08-15 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='univerbranch',
            name='logo',
            field=models.ImageField(blank=True, default='media/logo/logo_kstu.jpg', null=True, upload_to='media/logo/', verbose_name='Логотип'),
        ),
    ]
