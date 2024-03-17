from django.urls import path

from .views import UserViews

urlpatterns = [
    path("", UserViews.users_roles, name="users"),
    path("roles/", UserViews.assign_role, name="role"),
]
