from django.db import models
from device.models import Host

from django.utils.safestring import mark_safe
from django.core import urlresolvers 

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

    applevel = models.ForeignKey(Importance, blank=True, null=True)
    appowner = models.ManyToManyField(Owner, blank=True)
    host     = models.ManyToManyField(Host, blank=True)

    def __unicode__(self):
        return self.name
    
    def adminHostList(self):
        strOut = ""
        for h in self.host.all():
            strOut += '<a href="%s">%s</a>' % (urlresolvers.reverse('admin:device_host_change',args=(h.id,) ),h.adminList() ) + "<BR />" 
#                 h.name + "<BR />"
        return mark_safe(strOut)
    adminHostList.short_description = "Host list"