# Generated by Django 4.2.9 on 2024-01-05 12:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_alter_sensorreading_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="sensorreading",
            options={"ordering": ("-created_on",)},
        ),
    ]