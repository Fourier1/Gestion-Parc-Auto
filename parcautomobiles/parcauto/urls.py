# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url, include
from . import views
from parcauto.views import UserViewSet
from rest_framework import routers
from rest_framework.schemas import get_schema_view
# from rest_framework.documentation import include_docs_urls
# Routers provide an easy way of automatically determining the URL conf.
# ajouter un schema genere automatiquement

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
schema_view = get_schema_view(title='pastebin API')

urlpatterns = [

    url(r'^schema/$', schema_view),

    url(r'^docs/', include('rest_framework_docs.urls')),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^modeles/$', views.ModeleListe.as_view(), name='modeles'),
    url(r'^modeles/(?P<pk>[0-9]+)/$', views.ModeleDetail.as_view(), name='modeles-detail'),

    url(r'^reparations/$', views.ReparationListe.as_view()),
    url(r'^reparations/(?P<pk>[0-9]+)/$', views.ReparationDetail.as_view()),

    url(r'^garages/$', views.GarageListe.as_view()),
    url(r'^garages/(?P<pk>[0-9]+)/$', views.GarageDetail.as_view()),

    url(r'^vehicules/$', views.VehiculeListe.as_view()),
    url(r'^vehicules/(?P<pk>[0-9]+)/$', views.VehiculeDetail.as_view()),

    url(r'^carnets/$', views.CarnetListe.as_view()),
    url(r'^carnets/(?P<pk>[0-9]+)/$', views.CarnetDetail.as_view()),

    url(r'^revisions/$', views.RevisionListe.as_view()),
    url(r'^revisions/(?P<pk>[0-9]+)/$', views.RevisionDetail.as_view()),

]