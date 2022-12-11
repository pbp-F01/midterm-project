from django.urls import path
from auth.views import login_user, register_user, logout_user

app_name = "auth"

urlpatterns = [
    path("login", login_user, name="login"),
    path("register", register_user, name="register"),
    path("logout", logout_user, name="logout"),
]
