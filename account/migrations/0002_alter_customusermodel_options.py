# Generated by Django 4.1.7 on 2023-02-22 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customusermodel",
            options={
                "verbose_name": "Kullanici",
                "verbose_name_plural": "Kullanıcılar",
            },
        ),
    ]
