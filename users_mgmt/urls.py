from django.urls import path

from .views import UserViews

urlpatterns = [
    path("roles/", UserViews.assign_role, name="roles"),
]
