from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import UserCreateView, passthru, LandingView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', auth_views.login, name='login' ),
    url(r'^register/(?P<pk>\d+)/$', UserCreateView.as_view(), name='user_create_view'),
    url(r'^passthru/$', passthru, name='passthru'),
    url(r'^landing/$', LandingView.as_view(), name='landing_view')
]
