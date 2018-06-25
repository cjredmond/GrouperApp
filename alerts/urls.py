from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import AlertCreateView

urlpatterns = [
    url(r'^alert-create/$', AlertCreateView.as_view(), name='alert_create_view')
]
