from pyexpat import model
from django.db import models
from django.contrib.auth.models import User 
from landing.models import Profile

# Create your models here.

class NewsModel(models.Model):
    news_title = models.CharField(max_length=255)
    news_body = models.TextField(blank=True)
    news_source = models.URLField(max_length=500)
    news_image = models.URLField(max_length=500)
    news_published = models.CharField(max_length=255)
    
class CommentModel(models.Model):
    comments_substance = models.TextField(blank=True)
    user = models.ForeignKey(Profile, related_name="profile", on_delete=models.CASCADE,  use_natural_foreign_keys=True)
    news = models.ForeignKey(NewsModel, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
