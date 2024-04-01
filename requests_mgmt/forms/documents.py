from django import forms

class UploadDocuments(forms.Form):
    documents = forms.FileField(label="Subir documentos", widget=forms.ClearableFileInput(attrs={'class': 'simple-button'}))

