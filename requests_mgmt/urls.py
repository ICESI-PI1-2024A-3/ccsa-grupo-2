from django.urls import path
from . import views

urlpatterns = [
    path('new_request/', views.request_index, name = 'request_index'),
    path("new_request/charge_account/", views.charge_account, name = "charge_account" )
]