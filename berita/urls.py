from django.urls import path
from berita.views import show_landing_news, show_news, show_json, show_json_comment, add_comment, show_url, show_profile, show_roles

app_name='berita'

urlpatterns = [
    path('', show_landing_news, name='show_landing_news'), 
    path('news_page/<int:id>', show_news, name='headline_news'), 
    path('json/', show_json, name='json'), 
    path('news_page/json_comment/<int:id>', show_json_comment, name='json_comment'), 
    path('news_page/add_comment/<int:id>', add_comment, name='add_comment'), 
    path('show_url', show_url, name='show_url'), 
    path('show_profile', show_profile, name='show_profile'), 
    # path('show_roles', show_roles, name='show_roles')
]