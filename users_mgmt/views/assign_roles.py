from django.shortcuts import render
from django.views import View

from ..forms import UpdateRoleForm
from ..models import CustomUser as User


class AssignRolesView(View):
    template_name = "assign_roles.html"
    form_class = UpdateRoleForm

    def get(self, request):
        users = User.objects.all()
        forms = []
        for user in users:
            forms.append(
                self.form_class(initial={"role": user.role, "user_id": user.id})
            )
        users_and_forms = zip(users, forms)
        return render(
            request,
            self.template_name,
            {"user": request.user, "users_and_forms": users_and_forms},
        )

    def post(self, request):
        try:
            users = User.objects.all()
            forms = []
            for user in users:
                forms.append(
                    self.form_class(initial={"role": user.role, "user_id": user.id})
                )
            users_and_forms = zip(users, forms)
            user_id = request.POST.get("user_id")
            role = request.POST.get("role")
            user = User.objects.get(pk=user_id)
            user.role = role
            user.save()
            return render(
                request,
                self.template_name,
                {
                    "user": request.user,
                    "users_and_forms": users_and_forms,
                    "success": "Rol asignado correctamente",
                },
            )
        except ValueError:
            return render(
                request,
                self.template_name,
                {
                    "user": request.user,
                    "users_and_forms": users_and_forms,
                    "error": "Error al asignar el rol",
                },
            )
