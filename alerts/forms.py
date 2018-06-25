from django import forms
from .models import Alert

HOURS_ACTIVE_CHOICES = (('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6),
                        ('12', 12), ('18', 18), ('24', 24),)

class AlertCreateForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['headline', 'text', 'hours_active']
    headline = forms.CharField()
    text = forms.Textarea()
    hours_active = forms.ChoiceField(widget=forms.Select,
                                                 choices=HOURS_ACTIVE_CHOICES)
