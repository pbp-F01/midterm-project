from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.shortcuts import redirect
from penjualan.models import Laporan
from django.contrib.auth.decorators import login_required
from landing.models import Profile

# Create your views here.
@login_required(login_url='/landing/login/')
def show_dashboard(request):
        data = request.user.laporan_set.all()
        context = {
                'laporan': data,
        }

        if request.user.profile.investor():
                return render(request, "penjualan/dashboard_show.html", context)
        elif request.user.profile.pemilik():
                return render(request, "penjualan/dashboard.html", context)
        else:
                return render(request, "landing/home.html")


def show_json(request):
        data = Laporan.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/landing/login/')
def add_laporan(request):

        laporan = Laporan(nama_umkm=request.POST['nama_umkm'], 
                        date=request.POST['date'],
                        jumlah_terjual=request.POST['jumlah_terjual'],
                        revenue=request.POST['revenue'],
                        user=request.user)
                        
        laporan.save()
        return redirect('penjualan:show_dashboard')