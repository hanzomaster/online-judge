# Generated by Django 3.2.18 on 2024-08-22 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("judge", "0190_deprecate_old_notif_fields"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="organization",
            name="logo_override_image",
        ),
    ]