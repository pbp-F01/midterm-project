from django.shortcuts import render,redirect

from profileUMKM.models import ProfileUMKM
from . models import Review 
from . forms import ReviewForm

def home(request):
    items = ProfileUMKM.objects.all()
    print(items)
    context = {
        'items':items
    }
    return render(request, "home.html",context)


def rate(request, id):
    post = ProfileUMKM.objects.get(id=id)
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        author = request.POST.get('author')
        stars = request.POST.get('stars')
        comment = request.POST.get('comment')
        review = Review(author=author, stars = stars,  comment=comment , umkm=post)
        review.save()
        return redirect('reviewUMKM:success')

    form = ReviewForm()
    context = {
        "form":form

    }
    return render(request, 'rate.html',context)


def success(request):
    return render(request, "success.html")
