# Generated by Django 4.2.7 on 2023-11-27 09:12

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Todo",
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
                ("content", models.CharField(max_length=100)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("deadline", models.DateTimeField(null=True)),
                ("is_done", models.BooleanField()),
                ("tag", models.ManyToManyField(related_name="todos", to="to_do.tag")),
            ],
        ),
    ]
