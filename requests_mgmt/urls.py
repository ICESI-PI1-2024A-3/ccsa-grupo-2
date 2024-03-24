<<<<<<< HEAD
from django.contrib import admin
from django.urls import include, path

from requests_mgmt.views import RequestViews

urlpatterns = [
    path('show_requests/',RequestViews.showRequests,name='show_requests'),
    path('edit_request/<int:request_id>',RequestViews.edit_request,name='edit_request'),
    path('delete_request/<int:request_id>',RequestViews.delete_request,name='delete_request'),
    path('new_request/', RequestViews.request_index, name = 'request_index'),
    path("new_request/charge_account/", RequestViews.charge_account, name = "charge_account"),
    path("show_requests/request_details/<int:request_id>", RequestViews.detail_request, name='details')

]


=======
from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (
    ChargeAccountView,
    DeleteRequestView,
    DetailsRequestView,
    EditRequestView,
    HomeView,
    RequestsListView,
    RequestsView,
)

urlpatterns = [
    path("", login_required(RequestsListView.as_view()), name="requests_list"),
    path(
        "<int:request_id>",
        login_required(DetailsRequestView.as_view()),
        name="detail_request",
    ),
    path(
        "<int:request_id>/editar",
        login_required(EditRequestView.as_view()),
        name="edit_request",
    ),
    path(
        "<int:request_id>/eliminar",
        login_required(DeleteRequestView.as_view()),
        name="delete_request",
    ),
    path("nueva", login_required(RequestsView.as_view()), name="requests_index"),
    path(
        "cuenta de cobro",
        login_required(ChargeAccountView.as_view()),
        name="charge_account",
    ),
]
>>>>>>> dev
