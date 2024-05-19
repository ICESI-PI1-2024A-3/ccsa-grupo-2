from django import forms

from users_mgmt.models import CustomUser as User, Roles


class AddApproverForm(forms.Form):
    # request_id = forms.IntegerField(widget=forms.HiddenInput())
    # type = forms.CharField(widget=forms.HiddenInput())
    approvers = forms.ChoiceField(required=False, label="")

    def __init__(self, *args, **kwargs):
        selected_approver_id = kwargs.pop("selected_approver_id", None)
        super(AddApproverForm, self).__init__(*args, **kwargs)
        approver_role = Roles.objects.get(name="aprobador")
        approvers = User.objects.filter(role=approver_role)
        approver_choices = [(0, "Selecione un aprobador")] + [
            (approver.id, approver) for approver in approvers
        ]
        self.fields["approvers"].choices = approver_choices

        if selected_approver_id:
            self.fields["approvers"].initial = selected_approver_id


# class AddApproverForm(forms.Form):
#     approver_role = Roles.objects.get(name="aprobador")
#     approvers = User.objects.filter(role=approver_role)
#     approver_choices = [(approver.id, approver) for approver in approvers]
#     selected_approver_id = forms.ChoiceField(choices=approver_choices, required=False)
