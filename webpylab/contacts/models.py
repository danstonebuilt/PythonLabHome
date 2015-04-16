# -*- coding: iso-8859-1 -*-
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __unicode__(self):
        return '%' % self.name

    class Admin:
        pass