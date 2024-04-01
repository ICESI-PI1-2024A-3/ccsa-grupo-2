from django import forms   

class AdvanceRequest(forms.Form):

    request_date = forms.DateField(label = 'Fecha de solicitud', widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),)

    dependency = forms.CharField(label = "Dependencia: ",max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))

    destination_city = forms.CharField(label = "Ciudad de destino: ",max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))
    
    departure_date = forms.DateField(
        label="Fecha de salida: ",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )

    return_date = forms.DateField(
        label="Fecha de regreso: ",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )

    reason_trip = forms.CharField(
    label="Motivo de viaje:",
    widget=forms.Textarea(attrs={"class": "form-control", "rows": 6}))

    advance_currency = forms.ChoiceField(label='Moneda', choices=[('Pesos colombianos', 'Pesos colombianos'), ('Dólares', 'Dólares'), ('Euros', 'Euros')], widget=forms.Select(attrs={'class': 'form-control'})) 

    icesi_last_day_date = forms.DateField(
        label="Indique el último día que estará en Icesi antes de su viaje: ",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )


class ExpenseBudget(forms.Form):

    airport_transport = forms.CharField(label = "Transporte Aereopuerto: ",max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))

    local_transport = forms.CharField(label = "Transporte local: ",max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))

    feeding = forms.CharField(label = "Alimentación: ",max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))
    
    accommodation = forms.CharField(label = "Alojamiento: ",max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))

    departure_taxes = forms.CharField(label = "Impuestos de salida: ",max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))

    others = forms.CharField(label = "Otros: ",max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))