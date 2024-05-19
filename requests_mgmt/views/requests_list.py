from django.shortcuts import render
from django.views import View
from django.contrib import messages
from ..models import RequestStatus, Request
from users_mgmt.models import CustomUser as User
from ..forms import AssignManagerForm


class RequestsListView(View):
    template_name = "requests_list.html"
    form_class = AssignManagerForm

    @classmethod
    def create_statuses_if_not_exist(cls):
        if RequestStatus.objects.count() == 0:
            RequestStatus.objects.bulk_create(
                [
                    RequestStatus(status="Pendiente de Aceptación"),
                    RequestStatus(status="Revisión"),
                    RequestStatus(status="Aceptado"),
                    RequestStatus(status="Aprobado"),
                    RequestStatus(status="Rechazado"),
                ]
            )

    def get(self, request):
        self.create_statuses_if_not_exist()

        requests = Request.objects.all()
        status_filter = request.GET.get("status", None)
        if status_filter:
            requests = requests.filter(status__status=status_filter)

        forms = [self.form_class(initial={"manager": req.manager}) for req in requests]
        requests_and_forms = zip(requests, forms)

        return render(
            request, self.template_name, {"requests_and_forms": requests_and_forms}
        )

    def post(self, request):
        self.create_statuses_if_not_exist()
        try:
            request_id = request.POST.get("request_id")
            accounting_manager_id = request.POST.get("manager")
            print("request_id", request_id)
            print("accounting_manager_id", accounting_manager_id)
            if not request_id or not accounting_manager_id:
                raise ValueError("Missing request id or accounting manager id")

            request_to_assign = Request.objects.get(pk=request_id)
            accounting_manager = User.objects.get(pk=accounting_manager_id)
            print("request_to_assign", request_to_assign)
            print("accounting_manager", accounting_manager)
            request_to_assign.manager = accounting_manager
            request_to_assign.save()

            messages.success(request, "Gerente de contabilidad asignado correctamente")

        except Exception as e:
            messages.error(
                request,
                f"Ocurrió un error al asignar el gerente de contabilidad: {str(e)}",
            )

        requests = Request.objects.all()
        forms = [self.form_class(initial={"manager": req.manager}) for req in requests]
        requests_and_forms = zip(requests, forms)

        return render(
            request, self.template_name, {"requests_and_forms": requests_and_forms}
        )
