from django.urls import path

from .views import UserViews

urlpatterns = [
    path("login/", UserViews.login, name="login"),
    path("register/", UserViews.register, name="register"),
    path("", UserViews.home, name="home"),
]
