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
    UpdateReviewerView,
)

urlpatterns = [

    path("", login_required(RequestsListView.as_view()), name="requests_list"),
    path(
        "<int:request_id>",
        login_required(DetailsRequestView.as_view()),
        name="detail_request",
    ),
    path("update/<int:request_id>", login_required(UpdateReviewerView.as_view()),name="update_reviewer"),
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
