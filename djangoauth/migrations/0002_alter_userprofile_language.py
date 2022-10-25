# Generated by Django 4.1.2 on 2022-10-24 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djangoauth", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="language",
            field=models.PositiveSmallIntegerField(
                choices=[("0", "Ukrainian"), ("1", "English")], default=1
            ),
        ),
    ]