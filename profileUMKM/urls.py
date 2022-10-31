from django.urls import path
from profileUMKM import views

app_name = "profile-UMKM"

urlpatterns = [
    path("", views.list_profile_UMKM, name="list_profile_UMKM"),
    path("json/", views.list_profile_UMKM_json, name="list_profile_UMKM_json"),
    path("add/", views.create_profile_UMKM, name="create_profile_UMKM"),
    path("delete/<int:pk>/", views.delete_profile_UMKM, name="delete_profile_UMKM"),
]