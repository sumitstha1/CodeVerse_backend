# Generated by Django 4.2.2 on 2023-06-23 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="is_read",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="hire",
            name="is_accept",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="hire",
            name="is_read",
            field=models.BooleanField(default=False),
        ),
    ]
