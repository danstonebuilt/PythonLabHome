# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Megasena(models.Model):
    raffleNumber = models.CharField(max_length=10)
    dayOfWeak = models.CharField(max_length=50)
    month = models.CharField(max_length=50)
    n1 = models.CharField(max_length=2)
    n2 = models.CharField(max_length=2)
    n3 = models.CharField(max_length=2)
    n4 = models.CharField(max_length=2)
    n5 = models.CharField(max_length=2)
    n6 = models.CharField(max_length=2)

    def __str__(self):
        return  '%s %s' % (self.dayOfWeak, self.month)

    class Admin:
        pass
