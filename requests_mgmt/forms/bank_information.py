from django import forms


class BankInformation(forms.Form):
    CHOICES = [("corriente", "Corriente"), ("ahorro", "Ahorro")]
    bank_name = forms.CharField(
        label="Banco: ",
        max_length=200,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    account_number = forms.CharField(label="Numero de Cuenta : ")
    account_type = forms.ChoiceField(
        label="Tipo de cuenta: ", choices=CHOICES, widget=forms.RadioSelect
    )
    cex_no = forms.CharField(label="CEX No : ")
