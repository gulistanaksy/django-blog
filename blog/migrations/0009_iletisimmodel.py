# Generated by Django 4.1.7 on 2023-02-21 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_alter_yorummodel_options_alter_yorummodel_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="IletisimModel",
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
                ("email", models.EmailField(max_length=250)),
                ("isim_soyisim", models.CharField(max_length=150)),
                ("mesaj", models.TextField()),
                ("olusturulma_tarihi", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "İletişim",
                "verbose_name_plural": "İletişim",
                "db_table": "iletisim",
            },
        ),
    ]
