from django import forms


class NewChargeAccountForm(forms.Form):
    amount = forms.DecimalField(
        label="Monto $",
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    concept = forms.CharField(
        label="Concepto:", widget=forms.Textarea(attrs={"class": "form-control"})
    )
