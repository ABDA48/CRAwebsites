# Generated by Django 5.0.1 on 2024-05-08 11:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_alter_news_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="description",
            field=models.TextField(max_length=5000),
        ),
    ]
