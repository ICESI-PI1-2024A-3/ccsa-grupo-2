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
            forms.append(self.form_class(initial={"role": user.role}))
        print("user.id", user.id)
        users_and_forms = zip(users, forms)
        return render(
            request,
            self.template_name,
            {"user": request.user, "users_and_forms": users_and_forms},
        )

    def post(self, request):
        try:
            user_id = request.POST.get("user_id")
            role = request.POST.get("role")

            if not user_id or not role:
                raise ValueError("Missing user id or role")

            user = User.objects.get(pk=user_id)

            if not user:
                raise ValueError("User not found")

            if role not in [
                "Process Leader",
                "Accounting Manager",
                "Requester",
                "Reviewer",
                "Approver",
            ]:
                raise ValueError("Invalid role")

            user.role = role
            user.save()

            users = User.objects.all()
            forms = []
            for user in users:
                forms.append(self.form_class(initial={"role": user.role}))
            users_and_forms = zip(users, forms)

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
            users = User.objects.all()
            forms = []
            for user in users:
                forms.append(self.form_class(initial={"role": user.role}))
            users_and_forms = zip(users, forms)
            return render(
                request,
                self.template_name,
                {
                    "user": request.user,
                    "users_and_forms": users_and_forms,
                    "error": "Error al asignar el rol",
                },
            )
