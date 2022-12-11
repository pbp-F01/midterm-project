from cgitb import reset
import datetime
from .models import Profile
from .forms import SignUp
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.contrib.auth.backends import UserModel

# Create your views here.


def index(request):
    return render(request, 'home.html')


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(
        reverse("landing:login"))
    response.delete_cookie('last_login')
    return response


def register_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        full_name = data["full_name"]
        email = data["email"]
        password1 = data["password1"]
        password2 = data["password2"]
        status = data["status"]
        username = data["username"]

        if UserModel.objects.filter(username=username).exists():
            return JsonResponse({"status": "duplicate"}, status=401)

        if password1 != password2:
            return JsonResponse({"status": "pass failed"}, status=401)

        createUser = UserModel.objects.create_user(
            username=username,
            password=password1,
        )

        createUser.save()
        newUser = Profile.objects.create(
            user=createUser,
            email=email,
            status=status,
            full_name=full_name
        )

        newUser.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)


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


def login_flutter(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Redirect to a success page.
            return JsonResponse({
                "status": True,
                "message": "Successfully Logged In!"
                # Insert any extra data if you want to pass data to Flutter
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Failed to Login, check your email/password."
        }, status=401)


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


def show_roles(request):
    user = ""
    if request.user.is_authenticated:
        user = Profile.objects.filter(user=request.user)
    context = {
        'user': user,
        "is_authenticated": request.user.is_authenticated,
    }
    return render(request, "base.html", context)


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
