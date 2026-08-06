from django.contrib import admin
from quest.models import Quest, Event


# Register your models here.

@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'event')
    list_filter = ('title', 'description')
    search_fields = ('title',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'duration', 'cost', 'TIMES')
    list_filter = ('name', 'date', 'cost')
    search_fields = ('name',)
