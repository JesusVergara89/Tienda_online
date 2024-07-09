from django import forms

class contar_form(forms.Form):
    asunto=forms.CharField()
    email=forms.EmailField()
    mensaje=forms.CharField()