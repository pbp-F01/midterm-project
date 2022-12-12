from django.urls import path
from reviewUMKM import views

app_name = "reviewUMKM"

urlpatterns = [
    path("", views.home, name="index"),
    path("success", views.success, name="success"),
    path("rate/<int:id>", views.rate, name="rate"),
    path("rate_flutter/<int:idUmkm>/<int:idUser>", views.rate_flutter, name="rate_flutter"),
    path("home/", views.success, name="home"),
    path("json/", views.show_rating_json, name="show_rating_json"),
    path("<int:id>/", views.show_json_by_id, name="show_json_by_id"),
]
