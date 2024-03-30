from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views import View

from ..backends import CustomAuthBackend
from ..forms import LoginForm


class LoginView(View):
    form_class = LoginForm
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = CustomAuthBackend().authenticate(
            request, username=username, password=password
        )
        if user is None:
            return render(
                request,
                self.template_name,
                {
                    "form": self.form_class(),
                    "error": "Usuario o contraseña incorrectos",
                },
            )
        else:
            login(request, user)
            return redirect("home")
