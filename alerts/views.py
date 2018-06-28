from django.shortcuts import render
from django.views.generic import *
from django.views.generic.edit import *
from django.contrib.auth import get_user_model
from django.urls import reverse

from .forms import AlertCreateForm
from .models import Alert

from group.models import Entity

import datetime
from django.utils import timezone

class AlertCreateView(CreateView):
    model = Alert
    form_class = AlertCreateForm
    def form_valid(self,form,**kwargs):
        instance = form.save(commit=False)
        instance.entity = Entity.objects.get(slug=self.kwargs['slug'])
        instance.expiration_time = timezone.now() + datetime.timedelta(hours=instance.hours_active)
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('landing_view')
