from django.db import models

class Table(models.Model):
    TABLE_SHAPES = (
        ('rectangle', 'Прямоугольный'),
        ('oval', 'Овальный'),
    )

    number = models.PositiveIntegerField("Номер стола", unique=True,primary_key=True,editable=False,auto_created=True )
    seats = models.PositiveIntegerField("Количество мест")
    shape = models.CharField("Форма стола", max_length=10, choices=TABLE_SHAPES)
    horizontal_coordinate = models.PositiveIntegerField("Координата по горизонтали")
    vertical_coordinate = models.PositiveIntegerField("Координата по вертикали")
    width = models.PositiveIntegerField("Ширина стола")
    length = models.PositiveIntegerField("Длина стола")

    def __str__(self):
        return f"Стіл №{self.number}"

class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name="Стол")
    date = models.DateField("Дата бронювання")
    name = models.CharField("Ім'я", max_length=50)
    email = models.EmailField("Email")

    class Meta:
        unique_together = ('table', 'date')

    def __str__(self):
        return f"Бронювання {self.table} на {self.date}"