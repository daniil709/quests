from django.contrib import admin

from quest.forms import CakeForm
from quest.models import Quest, Event, Employee, Book, Team, Cake


@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'event', 'duration', 'cost', 'TIMES')
    list_filter = ('title', 'description')
    search_fields = ('title',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'employee')
    list_filter = ('name', 'start_date', 'end_date')
    search_fields = ('name',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'job', 'salary')
    list_filter = ('name', 'age', 'job')
    search_fields = ('name', 'age', 'salary', 'job')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pages', 'price')
    list_filter = ('title', 'author', 'price')
    search_fields = ('title', 'author', 'pages', 'price')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'event')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'calorie', 'cost')
    list_filter = ('name',)
    search_fields = ('name',)