import datetime
import profile
from .models import Profile
from .forms import SignUp
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    form = SignUp()

    if request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            pengguna = form.save()
            profile.objects.create(user=pengguna, name=form.get('name'), email=form.get('email'), roles=form.get('roles'))
            messages.success(request, 'Akun berhasil dibuat!')
            return redirect('landing:login')

    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)
