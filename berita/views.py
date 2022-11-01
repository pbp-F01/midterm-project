from datetime import datetime
from time import timezone
from django.shortcuts import render
from berita.models import NewsModel
from berita.models import CommentModel
from landing.models import Profile
from django.http import HttpResponse
import datetime
from django.core import serializers
from django.http import Http404
from django.contrib.auth.decorators import login_required
from landing.models import Profile
from django.contrib.auth import authenticate

# Create your views here.

# @login_required(login_url='/landing/login/')
def show_landing_news(request):
    news = NewsModel.objects.all()
    context = {
        'berita': news, 
    }
    return render(request, 'news_landing_page.html', context)

def show_news(request, id):
    berita = NewsModel.objects.filter(pk=id)
    comments = CommentModel.objects.filter(news__pk=id)
    context = {
        'news': berita, 
        'comments': comments, 
    }
    return render(request, 'news_page.html', context)

def show_json(request):
    data = NewsModel.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# @login_required(login_url='/landing/login/')
def show_json_comment(request, id):
    data = CommentModel.objects.filter(news__pk=id)
    return HttpResponse(serializers.serialize("json", data, use_natural_foreign_keys=True), content_type="application/json")

def show_profile(request):
    data_profile = Profile.objects.all()
    return HttpResponse(serializers.serialize("json", data_profile), content_type="application/json")

@login_required(login_url='/landing/login/')
def add_comment(request, id):
    if (request.method == 'POST'):
        comments_substance = request.POST.get('comments_substance')
        try:
            news = NewsModel.objects.get(pk=id)
        except NewsModel.DoesNotExist:
            raise Http404("No Model matches")

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        if profile.roles == 'K':
            new_comment = CommentModel.objects.create(
                comments_substance=comments_substance, 
                user = profile, 
                news = news, 
                date_added = datetime.datetime.now(), 
            )

            new_comment.save()
            return HttpResponse("")
    return render (request, "news_page.html")

def show_url(request):
    return request.path_info
