from django.shortcuts import render, redirect
from profileUMKM.models import ProfileUMKM
from .models import Review
from .forms import ReviewForm
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from landing.models import Profile
from django.views.decorators.csrf import csrf_exempt


def home(request):
    user = ""
    if request.user.is_authenticated:
        user = Profile.objects.get(user=request.user)
    return render(
        request,
        "reviewUMKM/home.html",
        context={
            "user": user,
            "is_authenticated": request.user.is_authenticated,
        },
    )


def rate(request, id):
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        post = ProfileUMKM.objects.get(id=id)
        author = Profile.objects.get(user=request.user)
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")
        review = Review(author=author, rating=rating, comment=comment, umkm=post)
        review.save()
        return redirect("reviewUMKM:success")

    form = ReviewForm()
    context = {"form": form}
    return render(request, "reviewUMKM/rate.html", context)


@csrf_exempt
def rate_flutter(request):
    post = ProfileUMKM.objects.get(id=request.POST.get("idUmkm"))
    author = Profile.objects.get(user=3)
    rating = request.POST.get("rating")
    comment = request.POST.get("comment")
    review = Review(author=author, rating=rating, comment=comment, umkm=post)
    review.save()
    return JsonResponse({
            "status": True,
            }, status=200)


def success(request):
    return render(request, "reviewUMKM/success.html")


def show_json_by_id(request, id):
    ratingbyid = Review.objects.get(pk=id)
    return HttpResponse(
        serializers.serialize("json", [ratingbyid]), content_type="application/json"
    )


def show_rating_json(request):
    rating = Review.objects.all()
    return HttpResponse(
        serializers.serialize("json", rating), content_type="application/json"
    )
