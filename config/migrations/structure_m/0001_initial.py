# Generated by Django 5.0 on 2024-08-15 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniverBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Название филиала')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='media/logo/', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'employee',
                'verbose_name_plural': 'employees',
                'db_table': 'univer_branch',
            },
        ),
    ]
