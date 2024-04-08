from django.shortcuts import redirect, render
from django.views import View

from ..forms import (
    UserInfoForm,
    TravelExpensesRequest,
    ExpenseBudget,
    UploadDocuments
)

# from ..models import 

class TravelExpensesRequest(View):
    template_name = "requests/create_travel_expenses_request.html"
    user_info = UserInfoForm
    travel_expense_request = TravelExpensesRequest
    expense_budget = ExpenseBudget
    upload_documents = UploadDocuments

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            "user_info": self.user_info(),
            "travel_expense_info": self.travel_expense_request(),
            "expense_budget": self.expense_budget(),
            "upload_documents": self.upload_documents
        })