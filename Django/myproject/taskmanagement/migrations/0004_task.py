# Generated by Django 5.0.3 on 2024-04-18 18:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taskmanagement", "0003_user_user_type_alter_user_first_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("description", models.CharField(max_length=120)),
                ("start_date", models.DateField(blank=True, null=True)),
                ("end_date", models.DateField(blank=True, null=True)),
                (
                    "created_user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "members",
                    models.ManyToManyField(
                        related_name="tasks", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]
