# Generated by Django 4.1.1 on 2022-10-15 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Appblog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Curso",
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
                ("nombre", models.CharField(max_length=30)),
                ("comision", models.IntegerField()),
                ("fecha_de_inicio", models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Subscriptores",
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
                ("nombre", models.CharField(max_length=30)),
                ("apellido", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name="Seccion",
        ),
        migrations.AlterModelOptions(
            name="autor",
            options={"verbose_name_plural": "Autores"},
        ),
    ]
