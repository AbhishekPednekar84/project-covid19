# Generated by Django 3.0.4 on 2020-03-17 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("covid19_sections", "0006_auto_20200317_1034")]

    operations = [
        migrations.CreateModel(
            name="Country",
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
                ("country", models.CharField(max_length=100)),
                (
                    "national_helpline",
                    models.CharField(blank=True, max_length=100),
                ),
                (
                    "national_email",
                    models.EmailField(blank=True, max_length=254),
                ),
                ("country_abbr", models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name="helpline",
            name="country",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="covid19_sections.Country",
            ),
        ),
    ]
