from django.shortcuts import render
from django.views import View

from ..models import CustomUser as User
from requests_mgmt.models import Request

class ApproveAsApproverView(View):
    template_name = "approve_as_approver.html"
    
    def get(self, request):
        # Obtener todas las solicitudes asignadas al aprobador actual
        requests_to_approval = Request.objects.filter(approver=request.user.id)
        
        # Filtrar las solicitudes en estado de "Aceptado"
        approved_requests = requests_to_approval.filter(status__status="Aceptado")
        
        # Determinar si hay solicitudes en estado de "Aceptado"
        has_approved_requests = approved_requests.exists()
        
        return render(
            request, 
            self.template_name,
            {
                "requests_to_approval": approved_requests,  # Pasar solo las solicitudes en estado de "Aceptado"
                "has_approved_requests": has_approved_requests  # Pasar la variable que indica si hay solicitudes en estado de "Aceptado"
            }
        )
