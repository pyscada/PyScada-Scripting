# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-26 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Script",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("label", models.CharField(blank=True, default="", max_length=255)),
                ("active", models.BooleanField(default=True)),
                (
                    "interval",
                    models.FloatField(
                        choices=[
                            (0.1, "100 Milliseconds"),
                            (0.5, "500 Milliseconds"),
                            (1.0, "1 Second"),
                            (5.0, "5 Seconds"),
                            (10.0, "10 Seconds"),
                            (15.0, "15 Seconds"),
                            (30.0, "30 Seconds"),
                            (60.0, "1 Minute"),
                            (150.0, "2.5 Mintues"),
                            (300.0, "5 Minutes"),
                            (360.0, "6 Minutes (10 times per Hour)"),
                            (600.0, "10 Minutes"),
                            (900.0, "15 Minutes"),
                            (1800.0, "30 Minutes"),
                            (3600.0, "1 Hour"),
                        ],
                        default=5,
                    ),
                ),
                ("script_file", models.CharField(default="", max_length=255)),
            ],
        ),
    ]
