# Generated by Django 4.2 on 2024-01-26 03:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("foundation", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="foundation",
            name="name",
            field=models.CharField(default="", max_length=120, verbose_name="foundation name"),
        ),
    ]