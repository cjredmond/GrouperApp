from django.shortcuts import render
from django.views.generic import *
from django.views.generic.edit import *
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import MyUserCreateForm
from django.conf import settings
from django.contrib.auth import login

# from group.models import Entity

User = get_user_model()

def create_user_passthru(request):
    user = User.objects.last()
    login(request, user, backend=settings.AUTHENTICATION_BACKENDS[0])
    return HttpResponseRedirect(
        reverse('landing_view',
            )
    )


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
        return reverse('create_user_passthru')

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

class RegisterChoiceView(TemplateView):
    template_name = 'register_choice_view.html'

# x = User.objects.get(username='firstuser')
# print(x.get_alerts)
