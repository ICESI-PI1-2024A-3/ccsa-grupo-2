from django import forms


class TaxTreatmentForm(forms.Form):
    CHOICES = [
        (
            "392_401",
            "Retención en la fuente artículos 392 y 401 del Estatuto Tributario",
        ),
        ("383", "Retención en la fuente artículo 383 del Estatuto Tributario"),
    ]
    checkbox_choices = forms.ChoiceField(
        label="Se tomarán costos y deducciones asociados a las rentas de trabajo por los servicios prestados:",
        choices=CHOICES,
        widget=forms.RadioSelect,
    )
