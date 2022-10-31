from django.contrib import admin
from berita.models import CommentModel, NewsModel

# Register your models here.
admin.site.register(CommentModel)
admin.site.register(NewsModel)
