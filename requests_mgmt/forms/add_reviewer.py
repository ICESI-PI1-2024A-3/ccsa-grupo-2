from django import forms

from users_mgmt.models import CustomUser as User, Roles


class AddReviewerForm(forms.Form):
    # request_id = forms.IntegerField(widget=forms.HiddenInput())
    # type = forms.CharField(widget=forms.HiddenInput())
    reviewers = forms.ChoiceField(required=False, label="")

    def __init__(self, *args, **kwargs):
        selected_reviewer_id = kwargs.pop("selected_reviewer_id", None)
        super(AddReviewerForm, self).__init__(*args, **kwargs)
        reviewer_role = Roles.objects.get(name="revisor")
        reviewers = User.objects.filter(role=reviewer_role)
        reviewer_choices = [(0, "Selecione un revisor")] + [
            (reviewer.id, reviewer) for reviewer in reviewers
        ]
        self.fields["reviewers"].choices = reviewer_choices

        if selected_reviewer_id:
            self.fields["reviewers"].initial = selected_reviewer_id


# class AddReviewerForm(forms.Form):
#     reviewer_role = Roles.objects.get(name="revisor")
#     reviewers = User.objects.filter(role=reviewer_role)
#     reviewer_choices = [(reviewer.id, reviewer) for reviewer in reviewers]
#     selected_reviewer_id = forms.ChoiceField(choices=reviewer_choices, required=False)
