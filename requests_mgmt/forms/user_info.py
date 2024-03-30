from django import forms


class UserInfoForm(forms.Form):
    DOCUMENT_CHOICES = [
        ("CC", "Cédula de ciudadanía"),
        ("TI", "Tarjeta de identidad"),
        ("CE", "Cédula de extranjería"),
    ]
    user_name = forms.CharField(
        label="Nombre de solicitante:",
        max_length=200,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    user_id = forms.CharField(
        label="Identificación solicitante (C.C.):",
        max_length=200,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    document_type = forms.ChoiceField(
        label="Tipo de documento:",
        choices=DOCUMENT_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
