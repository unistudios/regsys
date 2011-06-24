from django.db import models

# Create your models here.
class Level(models.Model):
    name = models.CharField(max_length=20)
        
    def __unicode__(self):
        return self.level

class Host(models.Model):
    name      = models.CharField(max_length=100)
    ipaddress = models.IPAddressField()
    
    level     = models.ForeignKey(Level)
    
    def __unicode__(self):
        return self.name
    
    
    # Change
