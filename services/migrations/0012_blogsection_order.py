# Generated by Django 4.2.2 on 2023-07-08 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0011_alter_blog_image_alter_blog_introduction_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogsection",
            name="order",
            field=models.IntegerField(null=True, unique=True),
        ),
    ]