from django.urls import path

from .views import UserViews

urlpatterns = [
    path("roles/", UserViews.assign_role, name="roles"),
    path("roles/search_users", UserViews.search_users, name="search_users"),
    path("solicitudes/", UserViews.show_approver, name="approvers"),
]
