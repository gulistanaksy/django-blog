# Generated by Django 4.1.7 on 2023-02-21 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_yorummodel"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="yorummodel",
            options={"verbose_name": "Yorum", "verbose_name_plural": "Yorumlar"},
        ),
        migrations.AlterModelTable(
            name="yorummodel",
            table="yorum",
        ),
    ]
