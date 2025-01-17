# Generated by Django 5.1.3 on 2025-01-04 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=100)),
                ("created_datetime", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField()),
            ],
        ),
    ]
