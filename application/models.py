from django.db import models
from device.models import Host

""" AppOwner """
class Owner(models.Model):
    name  = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.name

""" Application Level - Prod, QA, Dev, etc """
class Importance(models.Model):
    description = models.CharField(max_length=20)

    def __unicode__(self):
        return self.description

""" Application """
class Application(models.Model):
    name = models.CharField(max_length=100)

    applevel = models.ForeignKey(Importance, blank=True)
    appowner = models.ManyToManyField(Owner)
    host     = models.ManyToManyField(Host, blank=True)

    def __unicode__(self):
        return self.name