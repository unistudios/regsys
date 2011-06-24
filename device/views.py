from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_list, object_detail

from device.models import Host

def index(request):
    """ return all devices in the DB"""
    
    return object_list(request, queryset=Host.objects.all())