# Generated by Django 5.0.1 on 2024-05-24 13:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0015_rename_headline1_news_headline_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="description3",
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]