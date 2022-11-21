# Generated by Django 4.1.2 on 2022-11-21 21:37

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Dish",
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
                ("name", models.CharField(max_length=40)),
                ("description", models.TextField()),
                ("ingredients", models.TextField()),
                ("serving_size", models.IntegerField()),
                ("price", models.IntegerField()),
                (
                    "image",
                    django_resized.forms.ResizedImageField(
                        blank=True,
                        crop=None,
                        force_format=None,
                        keep_meta=True,
                        null=True,
                        quality=-1,
                        scale=None,
                        size=[150, 150],
                        upload_to="dishes",
                    ),
                ),
            ],
        ),
    ]
