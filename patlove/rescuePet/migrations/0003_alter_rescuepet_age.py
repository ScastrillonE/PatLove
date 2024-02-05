# Generated by Django 4.2 on 2024-01-30 23:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rescuePet", "0002_remove_rescuepet_adoption_fee_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rescuepet",
            name="age",
            field=models.CharField(
                choices=[("A", "ADULT"), ("K", "KITTEN"), ("Y", "YOUNG"), ("S", "SENIOR")],
                max_length=1,
                verbose_name="Age of rescue pet",
            ),
        ),
    ]
