# Generated by Django 4.2.2 on 2023-06-24 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="title",
            field=models.CharField(max_length=500),
        ),
    ]
