from django import forms
from .models import Event

class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'location', 'time', 'description']
    name = forms.CharField()
    location = forms.CharField()
    description = forms.Textarea()
    time = forms.DateTimeField(widget=forms.SplitDateTimeWidget)
