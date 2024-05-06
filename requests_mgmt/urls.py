from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (
    SearchRequestView,
    AdvanceRequest,
    AdvanceRequestView,
    ChargeAccountView,
    DeleteRequestView,
    DetailsRequestView,
    EditRequestView,
    HomeView,
    InvoiceLegalizationView,
    RequestsListView,
    RequestsMadeView,
    RequestsView,
    TravelExpensesRequest,
    UpdateApproverView,
    UpdateReviewerView,
    RequestExpenses,
    SetClosingDate
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
        "update_reviewer/<int:request_id>",
        login_required(UpdateReviewerView.as_view()),
        name="update_reviewer",
    ),
    path(
        "update_approver/<int:request_id>",
        UpdateApproverView.as_view(),
        name="update_approver",
    ),
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
    path(
        "nueva/legalizacion de facturas",
        login_required(InvoiceLegalizationView.as_view()),
        name="invoice_legalization",
    ),
    
    path(
        "nueva/anticipos",
        login_required(AdvanceRequestView.as_view()),
        name="advance_request",
    ),
    path(
        "<int:request_id>/nuevo gasto",
        login_required(RequestExpenses.as_view()),
        name="request_expense",
    ),
    path(
        "nueva/viaticos",
        login_required(TravelExpensesRequest.as_view()),
        name="travel_expenses",
    ),
    path(
        "mis solicitudes",
        login_required(RequestsMadeView.as_view()),
        name="requests_made",
    ),
    path(
        "<int:request_id>/Cierre",
        login_required(SetClosingDate.as_view()),
        name="set_closing_date",
    ),
    
]
