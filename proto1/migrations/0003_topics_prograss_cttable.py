# Generated by Django 4.1.7 on 2024-01-31 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("proto1", "0002_courses"),
    ]

    operations = [
        migrations.CreateModel(
            name="Topics",
            fields=[
                (
                    "Topic_ID",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("Topic_name", models.CharField(default="(*-*)", max_length=50)),
                ("Topic_description", models.CharField(max_length=1200, null=True)),
                ("Last_updated", models.DateTimeField(auto_now=True)),
                ("Topic_Sources", models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Prograss",
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
                ("Completed_topic_IDs", models.CharField(max_length=1000, null=True)),
                ("Incompleted_topic_IDs", models.CharField(max_length=1000, null=True)),
                ("Start_date", models.DateTimeField(auto_now=True)),
                ("Finish_date", models.DateTimeField(auto_now=True)),
                (
                    "Course_ID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prog_cid",
                        to="proto1.courses",
                    ),
                ),
                (
                    "User_ID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prog_uid",
                        to="proto1.trackeruser",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CTtable",
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
                ("Topics_IDs", models.CharField(max_length=10000, null=True)),
                ("Related_topic_IDs", models.CharField(max_length=10000, null=True)),
                ("Course_rating", models.IntegerField(default=0)),
                ("Recommended_Time", models.IntegerField(default=0)),
                (
                    "Course_ID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ct_cid",
                        to="proto1.courses",
                    ),
                ),
            ],
        ),
    ]