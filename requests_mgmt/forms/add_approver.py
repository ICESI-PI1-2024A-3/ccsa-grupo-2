from django import forms

from users_mgmt.models import CustomUser


class AddApproverForm(forms.Form):
    request_id = forms.IntegerField(widget=forms.HiddenInput())
    type =forms.CharField(widget=forms.HiddenInput())
    Aprovadores =forms.ChoiceField(required=False)

    def __init__(self, *args, **kwargs):
        super(AddApproverForm, self).__init__(*args, **kwargs)
        Aprovadores = CustomUser.objects.filter(role="Approver")
        approver_choices = [(approver.id, approver) for approver in Aprovadores]
        approver_choices.insert(0,('', '< selecione un aprovador >'))
        self.fields['Aprovadores'].choices =approver_choices