from django import forms


class form_formulario(forms.Form):

    curso = forms.CharField()
    comision = forms.IntegerField()
