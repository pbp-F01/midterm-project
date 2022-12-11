from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from landing.models import Profile
from landing.forms import SignUp


@csrf_exempt
def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            profile = Profile.objects.filter(user=user)
            # Redirect to a success page.
            return JsonResponse(
                {
                    "status": True,
                    "message": "Successfully Logged In!",
                    "user_data": {
                        "username": user.username,
                        "id": user.id,
                        "role": profile.roles,
                    },
                },
                status=200,
            )
        else:
            return JsonResponse(
                {"status": False, "message": "Failed to Login, Account Disabled."},
                status=401,
            )

    else:
        return JsonResponse(
            {
                "status": False,
                "message": "Failed to Login, check your username/password.",
            },
            status=401,
        )


@csrf_exempt
def register_user(request):
    if request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user,
                name=user.name,
                email=user.email,
                roles=user.roles,
            )
            return JsonResponse(
                {"status": True, "message": "Successfully create account!"},
                status=200,
            )
        return JsonResponse(
            {
                "status": False,
                "message": form.errors,
            },
            status=400,
        )


@csrf_exempt
def logout_user(request):
    logout(request)
    return JsonResponse(
        {"status": True, "message": "Akun berhasil log out!"}, status=200
    )
