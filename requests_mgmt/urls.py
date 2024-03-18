from django.urls import path
from . import views

urlpatterns = [
    path('new_request/', views.RequestViews.request_index, name = 'request_index'),
    path("new_request/charge_account/", views.RequestViews.charge_account, name = "charge_account" )
]