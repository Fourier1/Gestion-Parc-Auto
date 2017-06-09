# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
# ecriture du model des la base de données


class Modele(models.Model):
    nbPlace = models.IntegerField(verbose_name='Nombres de places')
    puissanceMod = models.IntegerField(verbose_name='puissance du model')
    carburant = models.CharField(max_length=25, verbose_name='Carburant')
    marqueMod = models.CharField(max_length=25, verbose_name='Marque du model')
    couleur = models.CharField(max_length=25, default='blanc', verbose_name='Couleur du model')


class Carnet(models.Model):
    motifIntervention = models.CharField(max_length=50, verbose_name='Motif d\' intervention')
    natureTravaux = models.CharField(max_length=50, verbose_name='Nature des travaux')
    dateFinTravaux = models.DateTimeField(verbose_name='Date de fin de travaux')
    kilometrage = models.FloatField(verbose_name='Kilométrage')
    imma = models.ForeignKey('Vehicule', null=True, on_delete=models.SET_NULL, related_name='vehicules', verbose_name='Immatriculation')


class Vehicule(models.Model):
    imma = models.CharField(max_length=25, unique=True, verbose_name='Immatriculation')
    anneeFabr = models.DateField(verbose_name='Année de fabrication')
    kilomatrage = models.IntegerField(verbose_name='Kilométrage', null=True)
    modeles = models.ForeignKey('Modele', on_delete=models.CASCADE, related_name='vehicules', verbose_name='Model du véhicule')
    carnets = models.ForeignKey('Carnet', on_delete=models.SET_NULL, null=True, related_name='vehicules', verbose_name='Carnet du  véhicule')


class Reparation(models.Model):
    natureReparation = models.CharField(max_length=25, verbose_name='Nature de la reparation')
    dateAccident = models.DateField(verbose_name='Date de l\'accidnet')
    dateFin = models.DateField(verbose_name='Date de fin de reparation')
    facture = models.FloatField(verbose_name='facture de la reparation')
    imma = models.ForeignKey('Vehicule', on_delete=models.CASCADE, related_name='raparations', verbose_name='immatriculation ')
    garages = models.ForeignKey('Garage', on_delete=models.SET_NULL, null=True, related_name='raparations')


class Revision(models.Model):
    natureRevision = models.CharField(max_length=25, verbose_name='Nature de la révision')
    dateFin = models.DateTimeField(auto_now=True, verbose_name='Date de fin de révision')
    facture = models.FloatField(verbose_name='Facture de la révision')
    vehicules = models.ForeignKey('Vehicule', on_delete=models.CASCADE, related_name='revisions')
    carnets = models.ForeignKey('Carnet', on_delete=models.CASCADE, related_name='revisions')
    garages = models.ForeignKey('Garage', on_delete=models.SET_NULL, null=True, related_name='revisions')


class Garage(models.Model):
    nomGarage = models.CharField(max_length=25, verbose_name='Nom du garage')
    nomGerant = models.CharField(max_length=25, verbose_name='Nom du gérant du garage')
    marqueGarage = models.CharField(max_length=25, verbose_name='marque du garage')


class Effectuer_1(models.Model):
    garages = models.ForeignKey('Garage', on_delete=models.CASCADE)
    revisions = models.ForeignKey('Revision', on_delete=models.CASCADE)


class Effectuer_2(models.Model):
    garages = models.ForeignKey('Garage', on_delete=models.CASCADE)
    reparations = models.ForeignKey('Reparation', on_delete=models.CASCADE)