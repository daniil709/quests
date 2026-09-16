from django.db import models

NULLABLE = {'blank': True, 'null': True}



class Employee(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя сотрудника')
    age = models.IntegerField(verbose_name='Возраст')
    job = models.CharField(max_length=100, verbose_name='Должность сотрудника')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Зарплата')

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


class Quest(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название квеста")
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, verbose_name='Событие')
    duration = models.DecimalField(verbose_name='Продолжительность', max_digits=5, decimal_places=2, default=1)
    cost = models.DecimalField(verbose_name='Стоимость', max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(verbose_name='Изображение', upload_to='quest_images/', default='quest_images/default.jpg', **NULLABLE)
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
