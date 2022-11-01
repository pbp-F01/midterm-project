from django.urls import path 
from .views import rate, home, success

app_name = "reviewUMKM"

urlpatterns = [
    path('',home, name="home"),
    path('success',success, name="success"),
    path('rate/<int:id>',rate,name="rate"),
]

