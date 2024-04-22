from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Usuario"}
        ),
    )
    password = forms.CharField(
        label="",
        max_length=100,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Contraseña"}
        ),
    )
