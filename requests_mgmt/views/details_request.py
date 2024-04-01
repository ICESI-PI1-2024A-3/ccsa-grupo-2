from django.shortcuts import render
from django.views import View

from ..forms import AddReviewerForm, AddApproverForm
from ..models import Request,ChargeAccountRequest


class DetailsRequestView(View):
    template_name = 'request_details.html'
    select_reviewer_form = AddReviewerForm
    select_approver_form = AddApproverForm

    def get(self, request,request_id, *args, **kwargs):
        intance_request=Request.objects.get(pk=request_id)
        return render(request, self.template_name,{
            'request':intance_request,
            'select_reviewer': self.select_reviewer_form(),
            'select_approver': self.select_approver_form()
        })       
