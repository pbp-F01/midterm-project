from pyexpat import model
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class NewsModel(models.Model):
    news_title = models.CharField(max_length=255)
    news_body = models.TextField(blank=True)
    news_source = models.CharField(max_length=255)
    news_image = models.URLField(max_length=500)
    
class CommentModel(models.Model):
    comments_substance = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(NewsModel, related_name="comments", on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
