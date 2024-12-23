# Generated by Django 4.2.4 on 2024-12-04 04:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("tourApi", "0010_delete_webinfo_remove_sitemain_address_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="imagebannermodel",
            options={},
        ),
        migrations.RemoveField(
            model_name="imagebannermodel",
            name="banner",
        ),
        migrations.AddField(
            model_name="imagebannermodel",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="imagebannermodel",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="imagebannermodel",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="banners/"),
        ),
        migrations.AlterModelTable(
            name="imagebannermodel",
            table=None,
        ),
    ]
