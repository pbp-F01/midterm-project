from datetime import datetime
from django.shortcuts import render
from berita.models import NewsModel
from berita.models import CommentModel
from django.http import HttpResponse
import datetime
from django.core import serializers


# Create your views here.

def show_landing_news(request):
    berita = NewsModel.objects.all()
    return render(request, "news_landing_page.html")

def show_headline_news(request, id):
    berita = NewsModel.objects.filter(pk=id)
    comments = CommentModel.objects.filter(news__pk=id)
    context = {
        'news': berita, 
        'comments': comments, 
    }
    return render(request, "headline_news.html", context)

def show_json(request):
    data = NewsModel.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_comment(request, id):
    data = CommentModel.objects.filter(news__pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def add_comment(request, id):
    if (request.method == 'POST'):
        comment_substance = request.POST.get('comments_substance')
        berita = NewsModel.objects.get(id=id)

        new_comment = CommentModel.objects.create(
            comment_substance=comment_substance, 
            user = request.user, 
            news = berita, 
            date_added = datetime.datetime.now(), 
        )

        new_comment.save()
        return HttpResponse("")
    return render (request, "headline_news.html")
