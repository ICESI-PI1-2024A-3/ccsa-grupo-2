from django import forms

from ..models import Roles

class UpdateRoleForm(forms.Form):
    # role = forms.ChoiceField(
    #     label="",
    #     choices=[
    #         "líder de proceso",
    #         "gestor de contabilidad",
    #         "solicitante",
    #         "revisor",
    #         "aprobador",
    #     ],
    #     widget=forms.Select(attrs={"class": "role-select"}),
    # )
    role = forms.ModelChoiceField(
        queryset=Roles.objects.all(),
        widget=forms.Select(attrs={"class": "role-select"})
    )