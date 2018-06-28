from django import forms
from .models import Event
from datetimewidget.widgets import DateTimeWidget

class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'location', 'time', 'description']
        widgets = {
        'time': DateTimeWidget(attrs={'id':'datetimeid'}, usel10n=True,bootstrap_version=3)
        }
    # name = forms.CharField()
    # location = forms.CharField()
    # description = forms.Textarea()
    # time = forms.DateTimeField(widget=forms.SplitDateTimeWidget)
