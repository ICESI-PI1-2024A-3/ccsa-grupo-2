from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import user_information, CreateNewChargeAccount

# Create your views here.

def request_index(request):
    return render(request, 'requests_index.html')

def charge_account(request):
    return render(request, "request_type/charge_account.html", {
        "user_form": user_information(),
        "charge_account": CreateNewChargeAccount()
    })