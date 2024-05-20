from django.shortcuts import redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.views import View
from ..models import Request, RequestStatus
from users_mgmt.models import CustomUser
from ..forms import AddReviewerForm

class UpdateReviewerView(View):

    def post(self, request, request_id, *args, **kwargs):
        form = AddReviewerForm(request.POST) 
        print("form", form)
        if form.is_valid(): 
            user_id = form.cleaned_data["reviewers"]
            print("user_id", user_id)
            if user_id != "0":  # Verificar si se ha seleccionado un revisor
                try:
                    instance_request = Request.objects.get(pk=request_id)
                    user = CustomUser.objects.get(pk=user_id)
                    instance_request.reviewer = user
                    instance_request.save()
                    
                    # Actualizar el estado de la solicitud a "Revisión"
                    new_status = RequestStatus.objects.get(status='Revisión')
                    instance_request.status = new_status
                    instance_request.save()
                    subject = 'Cambio de estado de solicitud'
                    recipient_list = user.email
                    template = f"Su solicitud ha sido asignada al Revisor {user}."
                    email = EmailMessage(
                    subject,
                    template,
                    settings.EMAIL_HOST_USER,
                    [recipient_list]
                    )
                    email.fail_silently=False
                    email.send()
            
                    return redirect("detail_request", request_id=request_id)
                    
                except (Request.DoesNotExist, CustomUser.DoesNotExist) as e:
                    instance_request = Request.objects.get(pk=request_id)
                    instance_request.reviewer = None
                    instance_request.save()
            else:
                # Si no se ha seleccionado un revisor, redirigir de vuelta a la página de detalles
                return redirect("detail_request", request_id=request_id) #, error="Debe seleccionar un revisor")
        else:
            # Si el formulario no es válido, redirigir de vuelta a la página de detalles
            return redirect("detail_request", request_id=request_id, error="Debe seleccionar un revisor")
