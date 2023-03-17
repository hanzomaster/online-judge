# Generated by Django 3.2.18 on 2023-02-20 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("judge", "0150_alter_profile_timezone"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="content_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.contenttype",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="comment",
            name="object_id",
            field=models.PositiveIntegerField(null=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="solution",
            name="problem",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="solution",
                to="judge.problem",
                verbose_name="associated problem",
            ),
        ),
        migrations.AddIndex(
            model_name="comment",
            index=models.Index(
                fields=["content_type", "object_id"],
                name="judge_comme_content_2dce05_idx",
            ),
        ),
    ]