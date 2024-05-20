from django import forms

from users_mgmt.models import CustomUser as User


class AssignManagerForm(forms.Form):
    manager = forms.ModelChoiceField(
        queryset=User.objects.filter(role__name="gestor de contabilidad"),
        widget=forms.Select(attrs={"class": "role-select"}),
    )
