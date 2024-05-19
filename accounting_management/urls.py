"""
URL configuration for accounting_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path

from requests_mgmt.views import HomeView
from users_mgmt.views import LoginView, LogoutView, RegisterView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("iniciar-sesión/", LoginView.as_view(), name="login"),
    path("registrarse/", RegisterView.as_view(), name="register"),
    path("cerrar-sesión/", login_required(LogoutView.as_view()), name="logout"),
    path("", login_required(HomeView.as_view()), name="home"),
    path("usuarios/", include("users_mgmt.urls")),
    path("solicitudes/", include("requests_mgmt.urls")),
]
