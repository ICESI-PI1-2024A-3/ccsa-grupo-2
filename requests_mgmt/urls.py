from django.contrib import admin
from django.urls import include, path

from requests_mgmt.views import RequestViews

urlpatterns = [
    path("charge_account_request/",RequestViews.createRequest,name='charge_account_request'),
    path('show_requests/',RequestViews.showRequests,name='show_requests'),
    path('detail_request/<int:request_id>',RequestViews.detail_request,name='detail_request'),
    path('edit_request/<int:request_id>',RequestViews.edit_request,name='edit_request'),
    path('delete_request/<int:request_id>',RequestViews.delete_request,name='delete_request')

]
