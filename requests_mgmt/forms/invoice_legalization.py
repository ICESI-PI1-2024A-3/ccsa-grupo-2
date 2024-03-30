from django import forms
from django.forms import formset_factory

class InvoiceLegalizationForm(forms.Form):
    legalization_date = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),)

    dependency = forms.CharField(label = "Dependencia: ",max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))

    destination_city = forms.CharField(label = "Dependencia: ",max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))

    departure_date = forms.DateField(
        label="Fecha de salida: ",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )

    reason_trip = forms.CharField(
    label="Motivo de viaje:",
    widget=forms.Textarea(attrs={"class": "form-control", "rows": 6})
)


class ExpenseRatioForm(forms.Form):
    rubro = forms.CharField(label='Rubro', max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))
    proveedor = forms.CharField(label='Proveedor',max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))
    nit = forms.CharField(label='Nit', max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))
    concepto = forms.CharField(label='Concepto', max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))
    anticipo_tipo = forms.ChoiceField(label='Moneda', choices=[('Pesos colombianos', 'Pesos colombianos'), ('Dólares', 'Dólares'), ('Euros', 'Euros')], widget=forms.Select(attrs={'class': 'form-control'}))


class BalanceDiscountAutorizationForm(forms.Form):
    CHOICES = [('si', 'Sí'), ('no', 'No')]
    autorizar_descuento = forms.ChoiceField(
        label="Autorizo el descuento en una sola cuota en el siguiente pago de nómina",
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-control'})
    )
