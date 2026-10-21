from django.contrib import admin
from django.urls import path
from quest import views
from quest.apps import QuestConfig

app_name = QuestConfig.name

urlpatterns = [
    path("", views.home, name="home"),
    path("catalog/", views.catalog, name="catalog"),
    path("quest_detail/<int:pk>", views.quest_detail, name="quest_detail"),
    path("books/", views.get_books, name="books"),
    path("event/", views.event_list, name="events"),
    path("employee_info/", views.employee_info, name="employee_info"),
    path("employee/<int:employee_id>", views.employee_detail, name="employee_detail"),
    path("events/create/", views.event_create, name="event_create"),
    path("assign-team/", views.assign_team_event, name="assign_team_event"),
    path("cakes/", views.create_cake, name="cake_create"),
]
