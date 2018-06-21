from django.shortcuts import render
from django.views.generic import *
from django.views.generic.edit import *
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreateForm
from django.urls import reverse
from django.http import HttpResponseRedirect

from group.models import Entity

User = get_user_model()
class UserCreateView(CreateView):
    model = User
    form_class = MyUserCreateForm
    def form_valid(self,form,**kwargs):
        instance = form.save(commit=False)
        print(self.kwargs['pk'])
        if self.kwargs['pk'] == '1':
            instance.level = 'm'
        else:
            instance.level = 'l'
        instance.username = instance.email
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('login')

@login_required
def passthru(request):
    return HttpResponseRedirect(
        reverse('landing_view',
            )
    )

class LandingView(TemplateView):
    def get_template_names(self):
        if self.request.user.level == 'm':
            return 'landing_member.html'
        else:
            return 'landing_leader.html'

# x = User.objects.get(username='firstuser')
# print(x.get_alerts)
