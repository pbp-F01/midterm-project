from cgitb import reset
import datetime
from .models import Profile
from .forms import SignUp
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core import serializers

# Create your views here.


def index(request):
    return render(request, 'home.html')


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(
        reverse("landing:login"))
    response.delete_cookie('last_login')
    return response


def register(request):
    form = SignUp()

    if request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            pengguna = form.save()
            Profile.objects.create(
                user=pengguna, name=pengguna.name, email=pengguna.email, roles=pengguna.roles)
            messages.success(request, 'Akun berhasil dibuat!')
            return redirect("landing:login")

    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(
                reverse("landing:index"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)


@login_required(login_url='/landing/login/')
def show_json(request):
    user = request.user
    data = Profile.objects.filter(user=user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


@login_required(login_url='/landing/login/')
def profile(request):
    user = request.user
    data = Profile.objects.filter(user=user)
    return render(request, 'profile.html', {'data': data})
