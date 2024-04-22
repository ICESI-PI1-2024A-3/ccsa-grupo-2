from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from ..models import(
    Request,
    invoice_legalization_request,
    invoice_expenses,
)

class RequestExpenses(View):
    def get(self, request, *args, **kwargs):
        print("\n!!!!!!ENTRA EN EXPENSES!!!!!!!!!\n")
        rubro = request.POST('rubro')
        print("\n RUBRO :",rubro)