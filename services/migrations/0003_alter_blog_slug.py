# Generated by Django 4.2.2 on 2023-06-24 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0002_alter_blog_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="slug",
            field=models.SlugField(blank=True, max_length=500, null=True, unique=True),
        ),
    ]
