from django.shortcuts import redirect, render

from .forms import LoginForm, RegisterForm
from .models import CustomUser as User


class UserViews:
    def home(request):
        return render(request, "index.html")

    def login(request):
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            print(username, password)
            return redirect("home")
        else:
            return render(request, "login.html", {"form": LoginForm()})

    def register(request):
        if request.method == "POST":
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            phone = request.POST.get("phone")
            id_type = request.POST.get("id_type")
            username = request.POST.get("id_number")
            email = request.POST.get("email")
            password = request.POST.get("password")
            print(
                first_name,
                last_name,
                phone,
                id_type,
                username,
                email,
                password,
            )
            return redirect("home")
        else:
            return render(request, "register.html", {"form": RegisterForm()})
