from django.shortcuts import render
from django.views import View
from django.db.models import Q

from ..models import (
    AdvanceRequest,
    ChargeAccountRequest,
    InvoiceLegalizationRequest,
    TravelExpenseRequest,
    RequestStatus,
    Request,
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
        requests = Request.objects.all()
        status_filter = request.GET.get('status', None)
        print("Status Filter:", status_filter)  # Agrega este print para depurar
        if status_filter:
            requests = Request.objects.filter(status__status=status_filter)
        else:
            requests = Request.objects.all()
        return render(request, self.template_name, {'requests': requests})
