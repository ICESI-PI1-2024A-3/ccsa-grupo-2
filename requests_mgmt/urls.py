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


