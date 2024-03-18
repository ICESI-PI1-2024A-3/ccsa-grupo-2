from django import forms


class user_information(forms.Form):

    DOCUMENT_CHOICES = [
        ('CC', 'Cédula de ciudadanía'),
        ('TI', 'Tarjeta de identidad'),
        ('CE', 'Cédula de extranjería'),
    ]

    user_name = forms.CharField(label="Nombre de solicitante:", max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))

    user_id = forms.CharField(label="Identificación solicitante (C.C.):", max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    document_type = forms.ChoiceField(label="Tipo de documento:", choices=DOCUMENT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    
    
class CreateNewChargeAccount(forms.Form):

    amount = forms.DecimalField(label="$", max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    concept = forms.CharField(label="Concepto:", widget=forms.Textarea(attrs={'class': 'form-control'}))

    costs_and_deductions = forms.BooleanField(label='Se tomarán costos y deducciones asociados a las rentas de trabajo por los servicios prestados : ',required=False)

    rent_tax_declarant = forms.BooleanField(label='Soy declarante del Impuesto de Renta : ',required=False)

    fiscal_resident = forms.BooleanField(label='Soy residente fiscal en Colombia',required=False)
    city = forms.CharField(label='Ciudad : ')
    date = forms.DateField(label='Fecha : ')
    bank_name = forms.CharField(label='Nombre del Banco :')
    account_type = forms.CharField(label='Tipo de Cuenta : ')
    account_number = forms.CharField(label='Numero de Cuenta : ')
    CEX_no = forms.CharField(label='CEX No : ')

class Assign_reviewer(forms.Form):
        assign_reviewer = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'}))





