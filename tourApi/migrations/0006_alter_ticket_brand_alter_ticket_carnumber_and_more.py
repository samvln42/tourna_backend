# Generated by Django 5.0.6 on 2024-05-30 09:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tourApi", "0005_alter_guide_category_alter_hotel_category_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="brand",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="ticket",
            name="carnumber",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="ticket",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]