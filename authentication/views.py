from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from landing.models import Profile
from landing.forms import SignUp
from django.contrib.auth.backends import UserModel
import json


@csrf_exempt
def login_user(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")
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
                            "role": str(profile.values()[0]['roles']),
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
    if request.method == 'POST':

        data = json.loads(request.body)

        name = data["name"]
        email = data["email"]
        password1 = data["password1"]
        password2 = data["password2"]
        roles = data["roles"]
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
            roles=roles,
            name=name
        )

        newUser.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)


@csrf_exempt
def logout_user(request):
    logout(request)
    return JsonResponse(
        {"status": True, "message": "Akun berhasil log out!"}, status=200
    )
