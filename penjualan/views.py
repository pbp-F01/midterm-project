from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from penjualan.models import Laporan
from django.contrib.auth.decorators import login_required
from landing.models import Profile
from django.views.decorators.csrf import csrf_exempt
from penjualan.forms import PenjualanForm

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

@csrf_exempt
def add_laporan_flutter(request):
    user = get_object_or_404(Profile, user=request.user)

    if request.method == "POST" and user.roles == "P":
        body = JsonResponse.loads(request.body.decode("utf-8"))
        form = PenjualanForm(body)

        if form.is_valid():
            form.cleaned_data["user"] = user
            data = form.cleaned_data
            PenjualanForm.objects.create(**data)

            return JsonResponse(
                {"status": True, "message": "Berhasil menambahkan Laporan Penjualan!"}
            )

        return JsonResponse({"status": False, "message": form.errors})