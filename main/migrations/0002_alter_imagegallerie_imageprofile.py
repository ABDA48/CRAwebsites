# Generated by Django 5.0.1 on 2024-05-08 08:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imagegallerie",
            name="imageprofile",
            field=models.ImageField(blank=True, null=True, upload_to="Gallery/"),
        ),
    ]
