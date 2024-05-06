from django.shortcuts import render
from django.views import View

from ..forms import UpdateRoleForm
from ..models import CustomUser as User


class SearchUsersView(View):
    template_name = "assign_roles.html"
    form_class = UpdateRoleForm

    def get(self, request):
        search_query = request.GET.get("search_query")
        if search_query:
            users = User.objects.filter(
                first_name__icontains=search_query
            ) | User.objects.filter(last_name__icontains=search_query)
        else:
            users = User.objects.all()

        if users.count() != 0:
            forms = [
                self.form_class(initial={"role": user.role, "user_id": user.id})
                for user in users
            ]
            users_and_forms = zip(users, forms)
            return render(
                request,
                self.template_name,
                {
                    "user": request.user,
                    "users_and_forms": users_and_forms,
                    "search_query": search_query,
                },
            )
        else:
            return render(
                request,
                self.template_name,
                {"user": request.user, "search_query": search_query},
            )
