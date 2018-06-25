from django import forms

class AlertForm(forms.form):
    headline = forms.CharField()
    text = forms.CharField()
    expiration_time = forms.
