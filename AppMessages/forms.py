from django import forms

class EnviarMensajeForm(forms.Form):
    emisor=forms.EmailField()
    receptor=forms.EmailField()
    cuerpoDelMensaje=forms.CharField(max_length=250)