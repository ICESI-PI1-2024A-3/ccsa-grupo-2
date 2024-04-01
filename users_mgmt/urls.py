from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import AssignRolesView, SearchUsersView, ApproveAsReviewerView

urlpatterns = [
    path("roles/", login_required(AssignRolesView.as_view()), name="assign_roles"),
    path(
        "roles/usuarios", login_required(SearchUsersView.as_view()), name="search_users"
    ),
    path("roles/revisores", login_required(ApproveAsReviewerView.as_view()), name="approve_as_reviewer"),
]
