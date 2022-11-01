from django.urls import path 
from .views import *

app_name = "reviewUMKM"

urlpatterns = [
    path('',home, name="home"),
    path('success',success, name="success"),
    path('rate/<int:id>',rate,name="rate"),
    path('home/',success, name="home"),
    path('json/',show_rating_json, name='show_rating_json'),
    path('<int:id>/', show_json_by_id, name='show_json_by_id'),
]

