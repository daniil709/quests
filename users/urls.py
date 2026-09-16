from django.urls import path
from users import views
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    # path("", views.UserCreateView.as_view(), name="register"),
]
