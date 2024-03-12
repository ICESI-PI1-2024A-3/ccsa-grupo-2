from django.urls import path

from .views import UserViews

urlpatterns = [
    path("", UserViews.home, name="home"),
]
