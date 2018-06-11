from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Entity

class EntityDetailView(DetailView):
    model = Entity

class EntityLookupView(View):
    # def get(self, request, code):
    #     target = Entity.objects.get(code=self.kwargs['code'])
    #     return HttpResponseRedirect( reverse('entity_detail_view', args=[str(target.id)]) )
    def post(self,request):
        code = str(request.POST['code'])
        try:
            target = Entity.objects.get(code=code)
        except ObjectDoesNotExist:
            return HttpResponseRedirect(reverse('landing_view'))
        return  HttpResponseRedirect(reverse('entity_detail_view', args=[str(target.id)]))
