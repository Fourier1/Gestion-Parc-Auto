# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from parcauto.models import *
from django.contrib.auth.models import User
# Serializers define the API representation.


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class ModeleSerializer(serializers.ModelSerializer):

    """Serialisation de touts champs de la table modele"""

    class Meta:
        model = Modele
        fields = ('id', 'nbPlace', 'puissanceMod', 'carburant', 'marqueMod', 'couleur')


class CarnetSerializer(serializers.ModelSerializer):
    """Serialisation de touts champs de la table carnet"""

    class Meta:
        model = Carnet
        fields = ('id', 'motifIntervention', 'natureTravaux', 'dateFinTravaux', 'kilometrage')


class ReparationSerializer(serializers.ModelSerializer):
    """Serialisation de touts champs de la table reparation"""

    class Meta:
        model = Reparation
        fields = ('id', 'natureReparation', 'dateAccident', 'dateFin', 'facture', 'imma', 'garages')


class RevisionSerializer(serializers.ModelSerializer):
    """serialisation de tous les champs de la table revision"""

    class Meta:
        model = Revision
        fields = ('id', 'natureRevision', 'dateFin', 'facture', 'vehicules', 'carnets', 'garages')


class VehiculeSerializer(serializers.ModelSerializer):
    """Serialisation de touts champs de la table Vehicule"""

    class Meta:
        model = Vehicule
        fields = ('id', 'imma', 'anneeFabr', 'kilomatrage', 'carnets', 'modeles')


class GarageSerializer(serializers.ModelSerializer):
    """ serialisation de tous les champs de la tables Garage"""

    class Meta:
        model = Garage
        fields = ('id', 'nomGarage', 'nomGerant', 'marqueGarage')



