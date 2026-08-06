from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    date = models.DateTimeField(verbose_name='Дата и время')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    duration = models.DecimalField(verbose_name='Продолжительность', max_digits=5, decimal_places=2, default=1)
    cost = models.DecimalField(verbose_name='Стоимость', max_digits=10, decimal_places=2)
    TIMES = {
        "Утро": ["11:00", "17:00"],
        "День": ["13:00", "15:00"],
        "Вечер": ["19:00"],

    }

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering = ['name']

    def __str__(self):
        return self.name


class Quest(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название квеста")
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, verbose_name='Событие')
    STATUS_CHOICES = [
        ('draft', 'Черновик'),
        ('active', 'Активен'),
        ('completed', 'Завершён'),
        ('canceled', 'Отменён'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft',
        verbose_name='Статус'
    )

    class Meta:
        verbose_name = 'Квест'
        verbose_name_plural = 'Квесты'
        ordering = ['title']

    def __str__(self):
        return self.title

    def is_active(self):
        return self.status == 'active'

    def complete(self):
        self.status = 'completed'
        self.save()


class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    budget = models.IntegerField(verbose_name='Бюджет', **NULLABLE)
    cabinet = models.IntegerField(verbose_name='Кабинет', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'
        ordering = ['name']


class Employee(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя сотрудника')
    age = models.IntegerField(verbose_name='Возраст')
    job = models.CharField(max_length=100, verbose_name='Должность сотрудника')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Зарплата')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, verbose_name='Команда')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название книги')
    pages = models.IntegerField(verbose_name='Кол-во страниц')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title']

    def __str__(self):
        return self.title
