from django.shortcuts import render
from django.views.generic import *
from django.views.generic.edit import *
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Event
from .forms import EventCreateForm

from group.models import Entity

class EventCreateView(CreateView):
    model = Event
    form_class = EventCreateForm
    def form_valid(self,form,**kwargs):
        instance = form.save(commit=False)
        instance.entity = Entity.objects.get(id=int(self.kwargs['group_id']))
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('landing_view')
