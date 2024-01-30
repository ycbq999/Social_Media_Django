# Generated by Django 5.0.1 on 2024-01-29 22:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="liked_by",
            field=models.ManyToManyField(
                blank=True, related_name="posts_liked", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="caption",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
