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

    amount = forms.DecimalField(label="Monto $", max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    concept = forms.CharField(label="Concepto:", widget=forms.Textarea(attrs={'class': 'form-control'}))

class TaxTreatmentForm(forms.Form):
    CHOICES = [
        ('392_401', 'Retención en la fuente artículos 392 y 401 del Estatuto Tributario'),
        ('383', 'Retención en la fuente artículo 383 del Estatuto Tributario'),
    ]

    checkbox_choices = forms.ChoiceField(
        label="Se tomarán costos y deducciones asociados a las rentas de trabajo por los servicios prestados:",
        choices=CHOICES,
        widget=forms.RadioSelect,  # Utilizamos RadioSelect para permitir solo una selección
    )

class CheckboxRentaResidente(forms.Form):
    declarante = forms.BooleanField(label="Soy declarante de impuesto de renta", required=False)
    
    residente = forms.BooleanField(label="Soy residente fiscal en Colombia", required=False)

class City_Date(forms.Form):
    city = forms.CharField(label = "Ciuadad: ", max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))

    date = forms.DateField(label="Fecha:", widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))


    