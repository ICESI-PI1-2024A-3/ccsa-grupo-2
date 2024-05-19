from django import forms
from django.core.validators import FileExtensionValidator


class UploadDocuments(forms.Form):
    documents = forms.FileField(
        label="Subir documentos",
        required=False,
        widget=forms.ClearableFileInput(attrs={"class": "simple-button"}),
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
    )
