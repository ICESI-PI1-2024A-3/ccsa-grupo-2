from django.shortcuts import redirect, render
from django.views import View

from ..forms import (
    UserInfoForm,
    AdvanceRequest,
    ExpenseBudget
)

# from ..models import 

class AdvanceRequest(View):
    template_name = "requests/create_advance_request.html"
    user_info = UserInfoForm
    advance_request_info = AdvanceRequest
    expense_budget = ExpenseBudget

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,{
            "user_info": self.user_info(),
            "advance_request_info": self.advance_request_info(),
            "expense_budget": self.expense_budget(),
        })