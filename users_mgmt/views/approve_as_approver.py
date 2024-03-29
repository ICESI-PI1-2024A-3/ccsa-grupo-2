from django.shortcuts import render
from django.views import View

from ..forms import UpdateRoleForm
from ..models import CustomUser as User

class approve_as_approver(View):
    template_name = "assign_roles.html"
    
    def get(self, request):
        
        return render(
            request, 
            self.template_name,
            {""}
        )
        
    # def post(self, request):
        