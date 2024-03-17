from django.contrib.auth import login, logout
from django.db import IntegrityError
from django.shortcuts import HttpResponse, redirect, render

from .backends import CustomAuthBackend
from .forms import LoginForm, RegisterForm, UpdateRoleForm
from .models import CustomUser as User


class UserViews:
    def home(request):
        return render(request, "layouts/base.html", {"user": request.user})

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
                return redirect("users")

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
                    return redirect("users")
                except IntegrityError:
                    return render(
                        request,
                        "register.html",
                        {"form": RegisterForm(), "error": "El usuario ya existe"},
                    )

    ### Update default mehtods to use
    def logout(request):
        logout(request)
        return redirect("login")

    def retrieve_all_users(request):
        users = User.objects.all()
        return HttpResponse(users)

    def retrieve_user(request, user_id):
        user = User.objects.get(pk=user_id)
        return HttpResponse(user)

    def update_user(request, user_id):
        user = User.objects.get(pk=user_id)
        user.first_name = "John"
        user.save()
        return HttpResponse(user)

    def delete_user(request, user_id):
        user = User.objects.get(pk=user_id)
        user.delete()
        return HttpResponse(user)

    def users_roles(request):
        users = User.objects.all()
        forms = []
        for user in users:
            forms.append(
                UpdateRoleForm(initial={"role": user.role, "user_id": user.id})
            )
        users_and_forms = zip(users, forms)
        return render(request, "roles.html", {"users_and_forms": users_and_forms})

    def assign_role(request):
        user_id = request.POST.get("user_id")
        role = request.POST.get("role")
        user = User.objects.get(pk=user_id)
        user.role = role
        user.save()
        return redirect("users")
