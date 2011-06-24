from django.db import models

# Create your models here.
""" Server Level - prod, dev, qa..."""
class Level(models.Model):
    description = models.CharField(max_length=20)
        
    def __unicode__(self):
        return self.description
""" server Function : app, db, oracle, cluster, file server..."""
class Function(models.Model):
    description = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.description



""" servers """
class Host(models.Model):
    name      = models.CharField(max_length=100)
    ipaddress = models.IPAddressField()
    
    # Relationships
    serverlevel     = models.ForeignKey(Level)
    serverfunction  = models.ManyToManyField(Function, blank=True)
    
    def __unicode__(self):
        return self.name
