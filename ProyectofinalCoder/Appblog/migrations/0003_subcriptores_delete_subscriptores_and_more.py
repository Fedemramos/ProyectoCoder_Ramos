# Generated by Django 4.1.1 on 2022-10-15 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Appblog", "0002_curso_subscriptores_delete_seccion_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subcriptores",
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
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name="Subscriptores",
        ),
        migrations.RenameField(
            model_name="curso",
            old_name="comision",
            new_name="camada",
        ),
    ]