from django import forms

class UploadDocuments(forms.Form):
    #documents = forms.FileField(label="Subir documentos", widget=forms.ClearableFileInput(attrs={'class': 'simple-button'}))
    documents = forms.FileField(label="Subir documentos", required=False, widget=forms.ClearableFileInput(attrs={'class': 'simple-button'})) # Documentos no obligatorios (para poder hacer pruebas)

