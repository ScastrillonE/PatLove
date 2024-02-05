# Generated by Django 4.2 on 2024-01-27 17:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("foundation", "0005_alter_foundation_logo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accountbank",
            name="qr",
            field=models.ImageField(blank=True, null=True, upload_to="qr_bank"),
        ),
        migrations.AlterField(
            model_name="foundation",
            name="logo",
            field=models.ImageField(null=True, upload_to="logos", verbose_name="Logo of foundation"),
        ),
    ]
