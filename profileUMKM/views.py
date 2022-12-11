import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core import serializers
from landing.models import Profile
from profileUMKM.models import ProfileUMKM
from profileUMKM.forms import ProfileUMKMForm


def list_profile_UMKM(request):
    form = ProfileUMKMForm()
    user = ""
    if request.user.is_authenticated:
        user = get_object_or_404(Profile, user=request.user)
    return render(
        request,
        template_name="profileUMKM/index.html",
        context={
            "form": form,
            "user": user,
            "is_authenticated": request.user.is_authenticated,
        },
    )


@login_required(login_url="/landing/login/")
def create_profile_UMKM(request):
    form = ProfileUMKMForm()
    user = get_object_or_404(Profile, user=request.user)

    if request.method == "POST" and user.roles == "P":
        body = json.loads(request.body.decode("utf-8"))
        form = ProfileUMKMForm(body)

        if form.is_valid():
            form.cleaned_data["pemilik"] = user
            data = form.cleaned_data
            profileUMKM = ProfileUMKM.objects.create(**data)

            data["pemilik"] = user.name
            content = {
                "fields": data,
                "pk": profileUMKM.pk,
            }
            return JsonResponse(content, status=201)

        else:
            print(form.errors)

    return HttpResponseRedirect(reverse("profile-UMKM:list_profile_UMKM"))


@login_required(login_url="/landing/login/")
def delete_profile_UMKM(request, pk):
    user = get_object_or_404(Profile, user=request.user)

    if request.method == "DELETE" and user.roles == "P":
        profile_UMKM = get_object_or_404(ProfileUMKM, id=pk)
        profile_UMKM.delete()
        return HttpResponse(status=204)


def list_profile_UMKM_json(request):
    data = ProfileUMKM.objects.all()
    return HttpResponse(
        serializers.serialize("json", data, use_natural_foreign_keys=True),
        content_type="application/json",
    )


def get_profile_UMKM_json(request, pk):
    data = ProfileUMKM.objects.filter(id=pk)
    return HttpResponse(
        serializers.serialize("json", data, use_natural_foreign_keys=True),
        content_type="application/json",
    )


def create_profile_UMKM_flutter(request):
    user = get_object_or_404(Profile, user=request.user)

    if request.method == "POST" and user.roles == "P":
        body = json.loads(request.body.decode("utf-8"))
        form = ProfileUMKMForm(body)

        if form.is_valid():
            form.cleaned_data["pemilik"] = user
            data = form.cleaned_data
            profileUMKM = ProfileUMKM.objects.create(**data)

            data["pemilik"] = user.name
            content = {
                "fields": data,
                "pk": profileUMKM.pk,
            }
            return JsonResponse(content, status=201)

        return JsonResponse({"status": False, "message": "Input tidak valid!"})


def delete_profile_UMKM_flutter(request, pk):
    user = get_object_or_404(Profile, user=request.user)

    if request.method == "DELETE" and user.roles == "P":
        profile_UMKM = get_object_or_404(ProfileUMKM, id=pk)
        profile_UMKM.delete()
        return JsonResponse({"status": True, "message": "Profil UMKM berhasil dihapus"})
