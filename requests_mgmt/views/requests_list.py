from django.shortcuts import render
from django.views import View
from requests_mgmt.models import *


class RequestsListView(View):
    template_name = "requests_list.html"

    def get(self, request):
        requests = ChargeAccountRequest.objects.all()
        
        if(len(Format.objects.all())==0):
            Format.objects.create(type = 'Cuenta de Cobro').save()
            Format.objects.create(type = 'Legalización de Facturas').save()
            Format.objects.create(type = 'Anticipos').save()
            Format.objects.create(type = 'Viáticos').save()
            Format.objects.create(type = 'Facturas').save()
        if(len(RequestStatus.objects.all())==0):
            RequestStatus.objects.create(status = 'Pendiente de Aceptación').save()
            RequestStatus.objects.create(status = 'Revisión').save()
            RequestStatus.objects.create(status = 'Aprobado').save()
            RequestStatus.objects.create(status = 'Aceptado').save()
            RequestStatus.objects.create(status = 'Rechazado').save()
        if(len(RequestType.objects.all())==0):
            RequestType.objects.create(type = 'Document Type').save()
        
        return render(request, self.template_name,{
            'requests':requests
        })
