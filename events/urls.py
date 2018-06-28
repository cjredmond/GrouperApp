from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import EventCreateView

urlpatterns = [
    # url(r'^event-create/(?P<group_id>\d+)/$', EventCreateView.as_view(), name='event_create_view')
    path('event-create/<slug:slug>/', EventCreateView.as_view(), name='event_create_view')

]
