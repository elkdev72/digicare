# Generated by Django 5.0 on 2023-12-09 08:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("care", "0004_alter_appointment_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Plan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("plan_names", models.CharField(max_length=10)),
                ("basic_plan", models.IntegerField()),
                ("standard_plan", models.IntegerField()),
                ("premium_plan", models.IntegerField()),
                ("platinum_plan", models.IntegerField()),
            ],
        ),
    ]