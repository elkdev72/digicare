# Generated by Django 5.0 on 2023-12-09 04:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("care", "0003_alter_appointment_accepted_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="date",
            field=models.CharField(max_length=20),
        ),
    ]
