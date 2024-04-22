from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre"}
        ),
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Apellido"}
        ),
    )
    phone = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Teléfono"}
        ),
    )
    id_type = forms.ChoiceField(
        label="",
        choices=[
            ("CC", "Cédula de Ciudadanía"),
            ("CE", "Cédula de Extranjería"),
            ("TI", "Tarjeta de Identidad"),
        ],
        widget=forms.Select(
            attrs={"class": "form-control", "placeholder": "Tipo de Documento"}
        ),
    )
    id_number = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "No. de Documento"}
        ),
    )
    email = forms.EmailField(
        label="",
        max_length=100,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Correo Electrónico"}
        ),
    )
    password = forms.CharField(
        label="",
        max_length=100,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Contraseña"}
        ),
    )
    password_confirm = forms.CharField(
        label="",
        max_length=100,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirmar Contraseña"}
        ),
    )
