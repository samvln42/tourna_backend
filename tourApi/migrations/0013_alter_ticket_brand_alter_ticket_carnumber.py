# Generated by Django 4.2.4 on 2024-12-05 07:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tourApi", "0012_alter_imagebannermodel_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="brand",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="carnumber",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]