from django.shortcuts import render
from django.views import View

from ..models import (
    AdvanceRequest,
    ChargeAccountRequest,
    InvoiceLegalizationRequest,
    TravelExpenseRequest,
    RequestStatus,
)


class RequestsListView(View):
    template_name = "requests_list.html"
    if(len(RequestStatus.objects.all())==0):
        RequestStatus.objects.create(status='Pendiente de Aceptación').save()
        RequestStatus.objects.create(status='Revisión').save()
        RequestStatus.objects.create(status='Aceptado').save()
        RequestStatus.objects.create(status='Aprobado').save()
        RequestStatus.objects.create(status='Rechazado').save()

    def get(self, request):
        requests = ChargeAccountRequest.objects.all()
        return render(request, self.template_name,{
            'requests':requests
        })
