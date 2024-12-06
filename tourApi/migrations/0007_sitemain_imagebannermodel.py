# Generated by Django 5.0.6 on 2024-05-30 09:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tourApi", "0006_alter_ticket_brand_alter_ticket_carnumber_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sitemain",
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
                ("logo", models.ImageField(blank=True, null=True, upload_to="media/")),
                ("email", models.CharField(max_length=200)),
                ("address", models.TextField(blank=True, null=True)),
                ("tel", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "qrcode",
                    models.FileField(
                        blank=True, null=True, upload_to="media/", verbose_name="qrcode"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "1. Site main",
                "db_table": "site",
            },
        ),
        migrations.CreateModel(
            name="ImagebannerModel",
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
                (
                    "image",
                    models.FileField(
                        blank=True, null=True, upload_to="media/", verbose_name="image"
                    ),
                ),
                (
                    "banner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tourApi.sitemain",
                        verbose_name="Sitemain",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "1.1. image banner list",
                "db_table": "ImageBannerModel",
            },
        ),
    ]