from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views import View

from ..forms import RegisterForm
from ..models import CustomUser as User, Roles


class RegisterView(View):
    form_class = RegisterForm
    template_name = "register.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request, *args, **kwargs):
        if request.POST.get("password") != request.POST.get("password_confirm"):
            return render(
                request,
                self.template_name,
                {"form": self.form_class(), "error": "Las contraseñas no coinciden"},
            )
        else:
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            phone = request.POST.get("phone")
            id_type = request.POST.get("id_type")
            id_number = request.POST.get("id_number")
            email = request.POST.get("email")
            password = request.POST.get("password")

            user_found = User.objects.filter(email=email)
            if user_found:
                return render(
                    request,
                    self.template_name,
                    {"form": self.form_class(), "error": "El email ya está registrado"},
                )
            else:
                user_found = User.objects.filter(id_number=id_number)
                if user_found:
                    return render(
                        request,
                        self.template_name,
                        {
                            "form": self.form_class(),
                            "error": "El número de identificación ya está registrado",
                        },
                    )
                else:
                    role = Roles.objects.get(name="solicitante")

                    user = User.objects.create(
                        first_name=first_name,
                        last_name=last_name,
                        phone=phone,
                        id_type=id_type,
                        id_number=id_number,
                        username=id_number,
                        email=email,
                        password=password,
                        role=role,
                    )
                    login(request, user)
                    return redirect("home")
