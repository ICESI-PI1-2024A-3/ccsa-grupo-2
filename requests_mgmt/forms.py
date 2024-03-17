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



    