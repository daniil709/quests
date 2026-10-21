from tkinter.constants import CASCADE

from django.conf import settings
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Cake(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название торта')
    weight = models.FloatField(verbose_name='Вес торта')
    calorie = models.FloatField(verbose_name='Калорийность')
    cost = models.FloatField(verbose_name='Стоимость')

    class Meta:
        verbose_name = 'Торт'
        verbose_name_plural = 'Торты'


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title']

    def __str__(self):
        return self.title


class Employee(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя сотрудника')
    age = models.IntegerField(verbose_name='Возраст')
    job = models.CharField(max_length=100, verbose_name='Должность сотрудника')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Зарплата')

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name='Пользователь',
        **NULLABLE
    )

    team = models.ForeignKey(
        'Team',
        on_delete=models.SET_NULL,
        verbose_name='Команда',
        **NULLABLE
    )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['name']

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    start_date = models.DateField(verbose_name='Дата начала', **NULLABLE)
    end_date = models.DateField(verbose_name='Дата окончания', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Сотрудник', **NULLABLE)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering = ['name']

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, verbose_name='Мероприятие', **NULLABLE)

    def __str__(self):
        return self.name


class Quest(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название квеста")
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, verbose_name='Событие')
    duration = models.DecimalField(verbose_name='Продолжительность', max_digits=5, decimal_places=2, default=1)
    cost = models.DecimalField(verbose_name='Стоимость', max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(verbose_name='Изображение', upload_to='quest_images/', default='quest_images/default.jpg',
                              **NULLABLE)
    TIMES = ['11:00', '12:00', '13:00', '17:00', '18:00']
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


class Booking(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя клиента')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='booking', verbose_name='Квест')
    peoples = models.PositiveIntegerField(default=1, verbose_name='Кол-во человек')
    date = models.DateField(verbose_name='Дата посещения')
    time = models.CharField(max_length=5, choices=[(t, t) for t in Quest.TIMES], verbose_name='Время')
    email = models.EmailField(verbose_name='Эл. почта', **NULLABLE)
    comment = models.CharField(max_length=500, verbose_name='Комментарий', **NULLABLE)
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('confirmed', 'Подтверждена'),
        ('done', 'Завершёна'),
        ('canceled', 'Отменёна'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name='Статус заявки'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    class Meta:
        verbose_name = 'Запись на квест'
        verbose_name_plural = 'Записи на квест'
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['quest', 'date', 'time'],
                condition=models.Q(status__in=['new', 'confirmed']),
                name='unique_active_booking_slot'
            ),
        ]

        indexes = [models.Index(fields=['quest', 'date', 'time']), ]

    def __str__(self):
        return f'{self.name}, {self.date}, {self.quest.title}, {self.time}'
