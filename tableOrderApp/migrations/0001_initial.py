# Generated by Django 5.0 on 2023-12-18 00:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Table",
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
                (
                    "number",
                    models.PositiveIntegerField(
                        unique=True, verbose_name="Номер стола"
                    ),
                ),
                ("seats", models.PositiveIntegerField(verbose_name="Количество мест")),
                (
                    "shape",
                    models.CharField(
                        choices=[("rectangle", "Прямоугольный"), ("oval", "Овальный")],
                        max_length=10,
                        verbose_name="Форма стола",
                    ),
                ),
                (
                    "horizontal_coordinate",
                    models.PositiveIntegerField(
                        verbose_name="Координата по горизонтали"
                    ),
                ),
                (
                    "vertical_coordinate",
                    models.PositiveIntegerField(verbose_name="Координата по вертикали"),
                ),
                ("width", models.PositiveIntegerField(verbose_name="Ширина стола")),
                ("length", models.PositiveIntegerField(verbose_name="Длина стола")),
            ],
        ),
        migrations.CreateModel(
            name="Reservation",
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
                ("date", models.DateField(verbose_name="Дата бронювання")),
                ("name", models.CharField(max_length=50, verbose_name="Ім'я")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                (
                    "table",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tableOrderApp.table",
                        verbose_name="Стол",
                    ),
                ),
            ],
            options={
                "unique_together": {("table", "date")},
            },
        ),
    ]
