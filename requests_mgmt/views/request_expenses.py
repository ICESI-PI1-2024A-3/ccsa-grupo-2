from django.shortcuts import redirect, render, HttpResponse
from django.views import View

from ..models import(
    Request,
    InvoiceLegalizationRequest,
    Expense
)


from ..forms import(
    ExpenseRatioForm
)

class RequestExpenses(View):
    template_name = "request_expense.html"
    def get(self, request,request_id, *args, **kwargs):
        instance_request = InvoiceLegalizationRequest.objects.get(pk=request_id)
        return render(
            request,
            self.template_name,
            {
                "request": instance_request,
                "user": request.user,
                "expense_ratio_form": ExpenseRatioForm
            },
        )
    def post(self, request, *args, **kwargs):
        request_id_number = request.POST.get("request_id")
        instance_request = Request.objects.get(pk=request_id_number)
        rubro = request.POST.get("rubro")
        proveedor = request.POST.get("proveedor")
        nit = request.POST.get("nit")
        concepto = request.POST.get("concepto")
        advance_currency = request.POST.get("advance_currency")
        amount = request.POST.get("amount")
        instance_expense = Expense.objects.create(
            request_id_number = instance_request,
            rubro = rubro,
            proveedor = proveedor,
            nit = nit,
            concepto = concepto,
            advance_currency = advance_currency,
            amount = amount,
        )
        instance_expense.save()

        return redirect("detail_request",request_id=request_id_number)
        