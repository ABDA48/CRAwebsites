# Generated by Django 5.0.1 on 2024-05-24 13:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0014_remove_news_description_remove_news_headline_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="news",
            old_name="headline1",
            new_name="headline",
        ),
        migrations.RemoveField(
            model_name="news",
            name="description3",
        ),
    ]