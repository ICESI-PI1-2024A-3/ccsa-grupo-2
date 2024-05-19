from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import (
    AssignRolesView,
    SearchUsersView,
    ApproveAsApproverView,
    ApproveAsReviewerView,
)

urlpatterns = [
    path("roles/", login_required(AssignRolesView.as_view()), name="assign_roles"),
    path("", login_required(SearchUsersView.as_view()), name="search_users"),
    path(
        "roles/aprobador",  # Deberia estar en requests_mgmt ???
        login_required(ApproveAsApproverView.as_view()),
        name="approve_as_approver",
    ),
    path(
        "roles/revisores",  # Deberia estar en requests_mgmt ???
        login_required(ApproveAsReviewerView.as_view()),
        name="approve_as_reviewer",
    ),
]
