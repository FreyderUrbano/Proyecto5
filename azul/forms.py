from cProfile import label
from dataclasses import fields
from logging import PlaceHolder
from django import forms
from azul.models import Case, Metodologia, Encuesta

# ********************************************************************************************
#   Formulario de registro de casos
# ********************************************************************************************


class EncuestaForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = ['question1', 'question2', 'question3', 'question4',
                  'question5', 'question6', 'question7', 'question8']


class CasesForm(forms.ModelForm):
    name = forms.CharField(label='Nombre de la empresa', widget=forms.TextInput(
        attrs={'class': 'clase1', 'placeholder': 'Nombre', }))
    nitempresa = forms.IntegerField(label='Nit de la empresa')
    rams = forms.CharField(label='Opcional si no aparece en la lista', widget=forms.TextInput(
        attrs={'class': 'clase4', 'placeholder': 'Opcional', }))
    detail = forms.CharField(label='Detalle del caso de infección', widget=forms.Textarea(
        attrs={'class': 'clase5', 'placeholder': 'Detalle del caso', }))
    imagen = forms.ImageField(label='Imagen evidencia de la infección')
    email = forms.CharField(label='Mensaje de rescate', widget=forms.Textarea(
        attrs={'class': 'clase6', 'placeholder': 'Se debe redactar o copiar el correo enviado como mensaje de rescate', }))
    wallet = forms.CharField(label='Billetera de rescate', widget=forms.TextInput(
        attrs={'class': 'clase7', 'placeholder': 'Moneda', }))

    class Meta:
        model = Case
        fields = ['name', 'nitempresa', 'rams',
                  'detail', 'imagen', 'email', 'wallet']

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        #self.fields['rams'].required = False
        self.fields['nitempresa'].widget.attrs.update(
            {'class': 'clase2', 'placeholder': '123456789', })


class ResetPasswordForm(forms.Form):
    user = forms.CharField(widget=forms.TextInput, label='Ingrese su username')


# ********************************************************************************************
#   Formulario de registro de metodologia
# ********************************************************************************************

class MetodologiaForm(forms.ModelForm):
    name = forms.CharField(label='Nombre', widget=forms.TextInput(
        attrs={'class': 'clase8', 'placeholder': 'Nombre', }))

    class Meta:
        model = Metodologia
        fields = ['name']
