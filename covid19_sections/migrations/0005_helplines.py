# Generated by Django 3.0.4 on 2020-03-17 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("covid19_sections", "0004_auto_20200311_1640")]

    operations = [
        migrations.CreateModel(
            name="Helplines",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("state", models.CharField(max_length=100)),
                ("helpline", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
            ],
        )
    ]
