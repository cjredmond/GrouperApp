from django.shortcuts import render
from django.views.generic import *
from django.views.generic.edit import *
from django.contrib.auth import get_user_model

from .models import Alert

class AlertCreateView(CreateView):
    model = Alert
    fields = ['headline', 'text', 'expiration_time']
    def form_valid(self,form,**kwargs):
        instance = form.save(commit=false)
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('landing_view')
