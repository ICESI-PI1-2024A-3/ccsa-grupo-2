from django.shortcuts import render
from .forms import *

# Create your views here.
class RequestViews:
    def createRequest(request):
        if request.method=='GET':
            return render(request,'createRequest.html',{
                'userInfoForm':user_information(),
                'inputForm':CreateNewChargeAccount()
            })
        
        

