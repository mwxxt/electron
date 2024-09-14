from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0002_alter_univerbranch_logo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='univerbranch',
            options={'verbose_name': 'Univer branch', 'verbose_name_plural': 'Univer branches'},
        ),
    ]
