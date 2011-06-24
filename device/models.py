from django.db import models

# Create your models here.
class Host(models.Model):
    name      = models.CharField(max_length=100)
    ipaddress = models.IPAddressField()
    
    def __unicode__(self):
        return self.name
    
class Level(models.Model):
    host  = models.ForeignKey(Host)
    level = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.level