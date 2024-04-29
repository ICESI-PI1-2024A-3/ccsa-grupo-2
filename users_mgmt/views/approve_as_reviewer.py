from django.shortcuts import render
from django.views import View

from ..models import CustomUser as User
from requests_mgmt.models import Request

class ApproveAsReviewerView(View):
    template_name = "approve_as_reviewer.html"
    
    def get(self, request):
        # Obtener todos los usuarios que necesitan aprobación
        # users_needing_approval = User.objects.filter(needs_approval=True)
        requests_to_approval = Request.objects.filter(reviewer=request.user.id)
        
        return render(
            request, 
            self.template_name,
            # {"users_needing_approval": users_needing_approval}
            {"requests_to_approval": requests_to_approval}
        )

    # def post(self, request):
    #     user_id = request.POST.get("user_id")
    #     action = request.POST.get("action")  # Aquí se podría definir algún campo en el formulario para la acción, como un botón de "aprobar"

    #     try:
    #         user = User.objects.get(pk=user_id)
    #         if action == "approve":
    #             # Lógica para aprobar al usuario
    #             user.approved = True
    #             user.save()
    #             message = "Usuario aprobado correctamente"
    #         elif action == "reject":
    #             # Lógica para rechazar al usuario
    #             user.approved = False
    #             user.save()
    #             message = "Usuario rechazado correctamente"
    #         else:
    #             message = "Acción no válida"

    #         # Obtener todos los usuarios que necesitan aprobación después de la acción realizada
    #         users_needing_approval = User.objects.filter(needs_approval=True)
    #         return render(
    #             request,
    #             self.template_name,
    #             {"users_needing_approval": users_needing_approval, "success": message},
    #         )
    #     except User.DoesNotExist:
    #         return render(
    #             request,
    #             self.template_name,
    #             {"error": "Usuario no encontrado"},
    #         )
