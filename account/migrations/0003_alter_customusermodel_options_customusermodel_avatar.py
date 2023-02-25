# Generated by Django 4.1.7 on 2023-02-24 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_alter_customusermodel_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customusermodel",
            options={
                "verbose_name": "Kullanıcı",
                "verbose_name_plural": "Kullanıcılar",
            },
        ),
        migrations.AddField(
            model_name="customusermodel",
            name="avatar",
            field=models.ImageField(blank=True, null=True, upload_to="avatar/"),
        ),
    ]
