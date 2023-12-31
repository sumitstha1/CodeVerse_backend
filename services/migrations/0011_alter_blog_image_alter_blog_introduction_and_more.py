# Generated by Django 4.2.2 on 2023-07-08 05:42

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0010_alter_service_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="image",
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name="blog",
            name="introduction",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="blogsection",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="blogsection",
            name="image",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="service",
            name="banner_image",
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name="service",
            name="image",
            field=models.URLField(),
        ),
    ]
