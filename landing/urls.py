from django.urls import path
from landing.views import *

app_name = 'landing'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', login_user, name='logout'),
]