from django.urls import path
from django.conf.urls import url, include
from .views import EntityLookupView, EntityDetailView, EntityUpdateView

urlpatterns = [
    url(r'^group/(?P<pk>\d+)$', EntityDetailView.as_view(), name="entity_detail_view"),
    url(r'^lookup/$', EntityLookupView.as_view(), name="entity_lookup_view"),
    path('group/<int:id>/<slug:slug>/update/', EntityUpdateView.as_view(), name='entity_update_view')
]
