# Generated by Django 4.1.2 on 2022-10-19 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djangoauth", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="language",
            field=models.CharField(
                choices=[("en", "ENGLISH"), ("uk", "UKRAINIAN")],
                default="uk",
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="phone_number",
            field=models.CharField(max_length=15),
        ),
    ]