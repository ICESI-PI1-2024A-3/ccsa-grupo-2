from django.urls import path

from .views import RequestViews

urlpatterns = [
    path("datails_request/", RequestViews.details_request, name="details"),
   
]