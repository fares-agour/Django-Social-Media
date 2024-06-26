# Generated by Django 5.0.3 on 2024-04-17 22:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0003_alter_profile_photo"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="follows",
        ),
        migrations.AddField(
            model_name="profile",
            name="friends",
            field=models.ManyToManyField(
                blank=True, related_name="friends", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
