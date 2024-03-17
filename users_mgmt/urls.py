from django.urls import path

from .views import UserViews

urlpatterns = [
    path("", UserViews.home, name="home"),
    path("roles/", UserViews.users_roles, name="roles"),
]
