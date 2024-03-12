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
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        id_type = request.POST.get("id_type")
        username = request.POST.get("id_number")
        email = request.POST.get("email")
        password = request.POST.get("password")
        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            id_type=id_type,
            username=username,
            email=email,
            password=password,
        )
        return render(
            request,
            "register.html",
            {
                "form": RegisterForm(),
            },
        )
