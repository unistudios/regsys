from django.db import models

""" AppOwner """
class Owner(models.Model):
    name  = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.name

""" Application Level - Prod, QA, Dev, etc """
class Level(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

""" Application """
class Application(models.Model):
    name = models.CharField(max_length=100)

    applevel = models.ForeignKey(Level)
    appowner = models.ForeignKey(Owner)

    def __unicode__(self):
        return self.name