from django import forms


class UpdateRoleForm(forms.Form):
    role = forms.ChoiceField(
        label="",
        choices=[
            ("Process Leader", "Lider de Proceso"),
            ("Accounting Manager", "Gestor de Contabilidad"),
            ("Requester", "Solicitante"),
            ("Reviewer", "Revisor"),
            ("Approver", "Aprobador"),
        ],
        widget=forms.Select(attrs={"class": "role-select"}),
    )
