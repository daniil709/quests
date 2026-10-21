from django.urls import path
from users import views
from users.apps import UsersConfig
from users.views import UserCreateView

app_name = UsersConfig.name

urlpatterns = [
    # path("", views.UserCreateView.as_view(), name="login"),
    path("register/", views.UserCreateView.as_view(), name="register"),
]
