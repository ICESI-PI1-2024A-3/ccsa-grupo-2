from django.conf import settings
from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from pathlib import Path
import os

class InvoicesRequestView(View):
    template_name = "requests/create_invoice_request.html"
    
    def get(self, request):
        return render(request, self.template_name)