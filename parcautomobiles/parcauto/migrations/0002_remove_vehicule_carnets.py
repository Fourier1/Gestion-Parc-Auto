# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 07:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parcauto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicule',
            name='carnets',
        ),
    ]