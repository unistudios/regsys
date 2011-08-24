from django.db import models

LENGTH_DESCRIPTION = 20

""" Server Level - prod, dev, qa..."""
# This has fixtures
class Servicelevel(models.Model):
    description = models.CharField(max_length=LENGTH_DESCRIPTION)
        
    def __unicode__(self):
        return self.description

""" server Function : app, db, oracle, cluster, file server..."""
# This has fixtures
class Function(models.Model):
    description = models.CharField(max_length=LENGTH_DESCRIPTION)
    
    def __unicode__(self):
        return self.description


""" server Operating System : Windows, Linux, Solaris """
# This has fixtures    
class OperatingSystem(models.Model):
    description = models.CharField(max_length=LENGTH_DESCRIPTION)

    def __unicode__(self):
        return self.description 

""" servers """
class Host(models.Model):
    name      = models.CharField(max_length=100)
    ipaddress = models.IPAddressField(blank=True, null=True)
    
    # Relationshipsa
    serverlevel     = models.ForeignKey(Servicelevel, default=6)
    serverfunction  = models.ManyToManyField(Function, blank=True)
    OS              = models.ForeignKey(OperatingSystem, default=1)
    
    def __unicode__(self):
        return self.name

    def adminList(self):
        return str(self.name) + " " + str(self.ipaddress)