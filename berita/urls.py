from django.urls import path
from berita.views import show_landing_news, show_headline_news, show_json, show_json_comment, add_comment

app_name='berita'

urlpatterns = [
    path('', show_landing_news, name='show_landing_news'), 
    path('headline_news/<int:id>', show_headline_news, name='headline_news'), 
    path('json/', show_json, name='json'), 
    path('headline_news/json_comment/<int:id>', show_json_comment, name='json_comment'), 
    path('add_comment/<int:id>', add_comment, name='add_comment'), 
]