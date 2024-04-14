from django import forms

from users_mgmt.models import CustomUser


class AddApproverForm(forms.Form):
    request_id = forms.IntegerField(widget=forms.HiddenInput())
    type = forms.CharField(widget=forms.HiddenInput())
    approvers = forms.ChoiceField(required=False, label="")

    def __init__(self, *args, **kwargs):
        super(AddApproverForm, self).__init__(*args, **kwargs)
        approvers = CustomUser.objects.filter(role="Approver")
        approver_choices = [(approver.id, approver) for approver in approvers]
        approver_choices.insert(0, ("", "< seleccione un aprovador >"))
        self.fields["approvers"].choices = approver_choices
