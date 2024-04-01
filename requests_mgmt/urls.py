from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (
    SearchRequestView,
    ChargeAccountView,
    DeleteRequestView,
    DetailsRequestView,
    EditRequestView,
    HomeView,
    RequestsListView,
    RequestsView,
    UpdateReviewerView,
    InvoiceLegalizationView,
    AdvanceRequest,
    TravelExpensesRequest,
    UpdateApproverView,
)

urlpatterns = [
    path("", login_required(RequestsListView.as_view()), name="requests_list"),
    path(
        "<int:request_id>",
        login_required(DetailsRequestView.as_view()),
        name="detail_request",
    ),
    path("search/<str:requester>", login_required(SearchRequestView.as_view()),name="search_request"),
    path(
        "<int:request_id>/editar",
        login_required(EditRequestView.as_view()),
        name="edit_request",
    ),
    path("update_reviewer/<int:request_id>",
        login_required(UpdateReviewerView.as_view()), name="update_reviewer"),

    path('update_approver/<int:request_id>',
        UpdateApproverView.as_view(), name='update_approver'),
    path(
        "<int:request_id>/eliminar",
        login_required(DeleteRequestView.as_view()),
        name="delete_request",
    ),
    path("nueva", login_required(RequestsView.as_view()), name="requests_index"),
    path(
        "nueva/cuenta de cobro",
        login_required(ChargeAccountView.as_view()),
        name="charge_account",
    ),
    path("nueva/legalizacion de facturas", login_required(InvoiceLegalizationView.as_view()), name="invoice_legalization"),
    path("nueva/adelanto", login_required(InvoiceLegalizationView.as_view()), name="advance_request"),
    path("nueva/legalizacion de facturas", login_required(InvoiceLegalizationView.as_view()), name="perdiem_request"),
    path("nueva/legalizacion de facturas", login_required(InvoiceLegalizationView.as_view()), name="invoice_legalization"),
    path("nueva/anticipos", login_required(AdvanceRequest.as_view()), name = "advance_request"),
    path("nueva/viaticos", login_required(TravelExpensesRequest.as_view()), name = "travel_expenses"),
]