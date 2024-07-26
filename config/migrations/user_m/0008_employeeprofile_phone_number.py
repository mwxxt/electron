# Generated by Django 5.0.7 on 2024-07-26 12:43

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0007_studentprofile_gender"),
    ]

    operations = [
        migrations.AddField(
            model_name="employeeprofile",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, null=True, region=None, unique=True
            ),
        ),
    ]
