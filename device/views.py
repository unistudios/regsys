from django.views.generic.list_detail import object_list
from django.http import HttpResponse
from django.core import serializers

from device.models import Host

def index(request):
    """ return all devices in the DB"""
    
    return object_list(request, queryset=Host.objects.all())

def data(request):
    return HttpResponse(serializers.serialize("json", Host.objects.all()), mimetype='text/javascript') 