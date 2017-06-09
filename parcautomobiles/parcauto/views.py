# -*- coding: utf-8 -*-
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import generics
# Create your views here.
# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
"""VEHICULE"""


class VehiculeListe(generics.ListCreateAPIView):
    """ Affichier la liste des vihicules """
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeSerializer


class VehiculeDetail(generics.RetrieveUpdateDestroyAPIView):
    """ appller les methodes retrive Destroy et Update """
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeSerializer

"""MODEL"""


class ModeleListe(generics.ListCreateAPIView):
    queryset = Modele.objects.all()
    serializer_class = ModeleSerializer


class ModeleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Modele.objects.all()
    serializer_class = ModeleSerializer

"""GARAGE"""


class GarageListe(generics.ListCreateAPIView):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer


class GarageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer

"""REPARATION"""


class ReparationListe(generics.ListCreateAPIView):
    queryset = Reparation.objects.all()
    serializer_class = ReparationSerializer


class ReparationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reparation.objects.all()
    serializer_class = ReparationSerializer

"""CARNET"""


class CarnetListe(generics.ListCreateAPIView):
    queryset = Carnet.objects.all()
    serializer_class = CarnetSerializer


class CarnetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carnet.objects.all()
    serializer_class = CarnetSerializer

"""REVISION"""


class RevisionListe(generics.ListCreateAPIView):
    queryset = Revision.objects.all()
    serializer_class = RevisionSerializer


class RevisionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Revision.objects.all()
    serializer_class = RevisionSerializer