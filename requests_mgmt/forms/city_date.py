from django import forms


class CityDateForm(forms.Form):
    city = forms.CharField(
        label="Ciudad: ",
        max_length=200,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    date = forms.DateField(
        label="Fecha: ",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )
