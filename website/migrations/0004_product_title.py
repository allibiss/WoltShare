# Generated by Django 4.1.3 on 2022-11-06 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0003_alter_customuser_lat_alter_customuser_lon"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="title",
            field=models.CharField(default="", max_length=512, verbose_name="Title"),
        ),
    ]
