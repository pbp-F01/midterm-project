from django.urls import path
from authentication.views import login_user, register_user, logout_user

app_name = "main"

urlpatterns = [
    path("login", login_user, name="login"),
    path("register", register_user, name="register"),
    path("logout", logout_user, name="logout"),
]
