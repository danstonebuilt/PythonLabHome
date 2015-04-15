# -*- coding: iso-8859-1 -*-
from django.db import models

# Create your models here.

class Megasena(models.Model):
    raffle_nbr = models.CharField(max_length=6)
    day_of_week = models.CharField(max_length=30)
    date = models.DateField()
    nbr_01 = models.IntegerField(default=0)
    nbr_02 = models.IntegerField(default=0)
    nbr_03 = models.IntegerField(default=0)
    nbr_04 = models.IntegerField(default=0)
    nbr_05 = models.IntegerField(default=0)
    nbr_06 = models.IntegerField(default=0)

    #def __unicode__(self):
        #return '%' %(self.day_of_week)

    class Admin:
        pass
