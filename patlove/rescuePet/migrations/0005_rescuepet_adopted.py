# Generated by Django 4.2 on 2024-01-31 01:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rescuePet", "0004_rescuepetphoto"),
    ]

    operations = [
        migrations.AddField(
            model_name="rescuepet",
            name="adopted",
            field=models.BooleanField(default=False, verbose_name="Adopted pet"),
        ),
    ]
