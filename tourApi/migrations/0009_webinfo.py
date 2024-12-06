# Generated by Django 4.2.4 on 2024-12-03 09:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tourApi", "0008_remove_guide_address"),
    ]

    operations = [
        migrations.CreateModel(
            name="WebInfo",
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
                    "logo",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="media/webinfo/",
                        verbose_name="logo image",
                    ),
                ),
                (
                    "banner1",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="media/webinfo/",
                        verbose_name="banner1 image",
                    ),
                ),
                (
                    "banner2",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="media/webinfo/",
                        verbose_name="banner2 image",
                    ),
                ),
                (
                    "banner3",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="media/webinfo/",
                        verbose_name="banner3 image",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name_plural": "Website Informations",
                "db_table": "WebInfo",
            },
        ),
    ]
