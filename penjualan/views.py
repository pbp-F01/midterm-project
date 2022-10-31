import re
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from penjualan.models import Laporan

# Create your views here.

def show_dashboard(request):
        data = Laporan.objects.all()
        context = {
                'laporan': data,
        }
        return render(request, "penjualan/dashboard.html", context)

def add_laporan(request):
        laporan = Laporan(nama_umkm=request.POST['nama_umkm'], 
                        date=request.POST['date'],
                        jumlah_terjual=request.POST['jumlah_terjual'],
                        revenue=request.POST['revenue'])
        laporan.save()
        return redirect('penjualan:show_dashboard')