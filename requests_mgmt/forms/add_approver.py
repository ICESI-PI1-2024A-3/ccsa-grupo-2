from django import forms

from users_mgmt.models import CustomUser


class AddApproverForm(forms.Form):
    # request_id = forms.IntegerField(widget=forms.HiddenInput())
    # type = forms.CharField(widget=forms.HiddenInput())
    approvers = forms.ChoiceField(required=False, label="")

    def __init__(self, *args, **kwargs):
        selected_approver_id = kwargs.pop("selected_approver_id", None)
        super(AddApproverForm, self).__init__(*args, **kwargs)
        approvers = CustomUser.objects.filter(role="Approver")
        approver_choices = [(0, "Selecione un aprobador")] + [
            (approver.id, approver) for approver in approvers
        ]
        self.fields["approvers"].choices = approver_choices

        if selected_approver_id:
            self.fields["approvers"].initial = selected_approver_id
