from django import forms

from users_mgmt.models import CustomUser


class AddReviewerForm(forms.Form):
    request_id = forms.IntegerField(widget=forms.HiddenInput())
    type = forms.CharField(widget=forms.HiddenInput())
    Revisores = forms.ChoiceField(required=False)

    def __init__(self, *args, **kwargs):
        super(AddReviewerForm, self).__init__(*args, **kwargs)
        Revisores = CustomUser.objects.filter(role="Reviewer")
        reviewer_choices = [(reviewer.id, reviewer) for reviewer in Revisores]
        reviewer_choices.insert(0,('', '< selecione un revisor >'))
        self.fields['Revisores'].choices = reviewer_choices
