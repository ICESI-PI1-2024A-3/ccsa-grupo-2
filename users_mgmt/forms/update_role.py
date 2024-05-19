from django import forms


class UpdateRoleForm(forms.Form):
    role = forms.ChoiceField(
        label="",
        choices=[
            "Líder de proceso",
            "Gestor de contabilidad",
            "Solicitante",
            "Revisor",
            "Aprobador",
        ],
        widget=forms.Select(attrs={"class": "role-select"}),
    )
