from django.urls import path, re_path
from . import views

app_name = 'penjualan'
urlpatterns = [
    path('', views.show_dashboard, name='show_dashboard'),
    path('addlaporan/', views.add_laporan, name='addlaporan'),
    path('json/', views.show_json, name='json'),
    path('addlaporanflut/', views.add_laporan_flutter, name='addlaporanflut'),
]