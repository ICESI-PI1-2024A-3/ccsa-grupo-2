from django import forms


class CheckboxRentResidentForm(forms.Form):
    rent_tax_declarant = forms.BooleanField(
        label="Soy declarante de impuesto de renta", required=False
    )
    fiscal_resident = forms.BooleanField(
        label="Soy residente fiscal en Colombia", required=False
    )
