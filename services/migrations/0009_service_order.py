# Generated by Django 4.2.2 on 2023-06-25 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0008_alter_service_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="order",
            field=models.IntegerField(null=True, unique=True),
        ),
    ]