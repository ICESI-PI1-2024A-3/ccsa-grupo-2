from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form_control", "placeholder": "Usuario"}
        ),
    )
    password = forms.CharField(
        label="",
        max_length=100,
        widget=forms.PasswordInput(
            attrs={"class": "form_control", "placeholder": "Contraseña"}
        ),
    )


class RegisterForm(forms.Form):
    first_name = forms.CharField(label="Nombre", max_length=100)
    last_name = forms.CharField(label="Apellido", max_length=100)
    phone = forms.CharField(label="Teléfono", max_length=20)
    id_type = forms.ChoiceField(
        label="Tipo de Documento",
        choices=[
            ("CC", "Cédula de Ciudadanía"),
            ("CE", "Cédula de Extranjería"),
            ("TI", "Tarjeta de Identidad"),
        ],
    )
    id_number = forms.CharField(label="No. de Documento", max_length=100)
    email = forms.EmailField(label="Correo Electrónico", max_length=100)
    password = forms.CharField(
        label="Contraseña", max_length=100, widget=forms.PasswordInput
    )
    password_confirm = forms.CharField(
        label="Confirmar Contraseña", max_length=100, widget=forms.PasswordInput
    )
