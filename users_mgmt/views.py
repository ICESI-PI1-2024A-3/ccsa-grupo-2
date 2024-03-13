from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import redirect, render

from .backends import CustomAuthBackend
from .forms import LoginForm, RegisterForm
from .models import CustomUser as User


class UserViews:
    def home(request):
        return render(request, "index.html")

    def login(request):
        if request.method == "GET":
            return render(request, "login.html", {"form": LoginForm()})
        else:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = CustomAuthBackend().authenticate(
                request, username=username, password=password
            )
            if user is None:
                return render(
                    request,
                    "login.html",
                    {"form": LoginForm(), "error": "Usuario o contraseña incorrectos"},
                )
            else:
                login(request, user)
                return redirect("home")

    def register(request):
        if request.method == "GET":
            return render(request, "register.html", {"form": RegisterForm()})
        else:
            if request.POST.get("password") != request.POST.get("password_confirm"):
                return render(
                    request,
                    "register.html",
                    {"form": RegisterForm(), "error": "Las contraseñas no coinciden"},
                )
            else:
                try:
                    first_name = request.POST.get("first_name")
                    last_name = request.POST.get("last_name")
                    phone = request.POST.get("phone")
                    id_type = request.POST.get("id_type")
                    id_number = request.POST.get("id_number")
                    email = request.POST.get("email")
                    password = request.POST.get("password")
                    user = User.objects.create(
                        first_name=first_name,
                        last_name=last_name,
                        phone=phone,
                        id_type=id_type,
                        username=id_number,
                        email=email,
                        password=password,
                    )
                    user.save()
                    login(request, user)
                    return redirect("home")
                except IntegrityError:
                    return render(
                        request,
                        "register.html",
                        {"form": RegisterForm(), "error": "El usuario ya existe"},
                    )

    def logout(request):
        logout(request)
        return redirect("login")
