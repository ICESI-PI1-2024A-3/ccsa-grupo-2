from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import HttpResponse, redirect, render

from .backends import CustomAuthBackend
from .forms import LoginForm, RegisterForm, UpdateRoleForm
from .models import CustomUser as User


class UserViews:
    @login_required
    def home(request):
        return render(request, "index.html")

    def custom_login(request):
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
                auth_login(request, user)
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
                    auth_login(request, user)
                    return redirect("home")
                except IntegrityError:
                    return render(
                        request,
                        "register.html",
                        {"form": RegisterForm(), "error": "El usuario ya existe"},
                    )

    @login_required
    def logout(request):
        logout(request)
        return redirect("login")

    def retrieve_all_users(request):
        users = User.objects.all()
        return HttpResponse(users)

    def update_user(request, user_id):
        user = User.objects.get(pk=user_id)
        user.first_name = "John"
        user.save()
        return HttpResponse(user)

    def delete_user(request, user_id):
        user = User.objects.get(pk=user_id)
        user.delete()
        return HttpResponse(user)

    @login_required
    def assign_role(request):
        users = User.objects.all()
        forms = []
        for user in users:
            forms.append(
                UpdateRoleForm(initial={"role": user.role, "user_id": user.id})
            )
        users_and_forms = zip(users, forms)
        if request.method == "GET":
            return render(
                request,
                "roles.html",
                {"user": request.user, "users_and_forms": users_and_forms},
            )
        elif request.method == "POST":
            try:
                user_id = request.POST.get("user_id")
                role = request.POST.get("role")
                user = User.objects.get(pk=user_id)
                user.role = role
                user.save()
                return render(
                    request,
                    "roles.html",
                    {
                        "user": request.user,
                        "users_and_forms": users_and_forms,
                        "success": "Rol asignado correctamente",
                    },
                )
            except ValueError:
                return render(
                    request,
                    "roles.html",
                    {
                        "user": request.user,
                        "users_and_forms": users_and_forms,
                        "error": "Error al asignar el rol",
                    },
                )

    def search_users(request):
        search_query = request.GET.get("search_query")
        users = User.objects.filter(
            first_name__icontains=search_query
        ) | User.objects.filter(last_name__icontains=search_query)
        forms = [
            UpdateRoleForm(initial={"role": user.role, "user_id": user.id})
            for user in users
        ]
        users_and_forms = zip(users, forms)
        return render(
            request,
            "roles.html",
            {
                "user": request.user,
                "users_and_forms": users_and_forms,
                "search_query": search_query,
            },
        )
        
    def show_approver(request):
        return render(
            request, 
            "approver.html"
        )
