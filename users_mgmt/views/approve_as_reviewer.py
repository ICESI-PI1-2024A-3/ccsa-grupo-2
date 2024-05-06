from django.shortcuts import render
from django.views import View

from ..models import CustomUser as User
from requests_mgmt.models import Request

class ApproveAsReviewerView(View):
    template_name = "approve_as_reviewer.html"
    
    def get(self, request):
        # Obtener todas las solicitudes asignadas al revisor actual
        requests_to_approval = Request.objects.filter(reviewer=request.user.id)
        
        # Filtrar las solicitudes en estado de "Revisión"
        review_requests = requests_to_approval.filter(status__status="Revisión")
        
        # Determinar si hay solicitudes en estado de "Revisión"
        has_review_requests = review_requests.exists()
        
        return render(
            request, 
            self.template_name,
            {
                "requests_to_approval": review_requests,  # Pasar solo las solicitudes en estado de "Revisión"
                "has_review_requests": has_review_requests  # Pasar la variable que indica si hay solicitudes en estado de "Revisión"
            }
        )
