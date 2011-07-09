# Create your views here.
from django.http import HttpResponse

from device.models import Host
from application.models import Application

def index(request):
    return HttpResponse("Not done yet")

def update(request):
    if request.method == 'POST':
        # try to get all our varialbes
        try:
            appname = request.POST['appname']
            servername  = request.POST['servername']
        except KeyError:
            return HttpResponse("Didn't provide all parameters")

        # add if necessary
        try:
            app = Application.objects.get(name=appname)
        except:
            app = Application(name=appname)
            app.save()
               
        try:
            server  = Host.objects.get(name=servername)
        except:
            server = Host(name=servername)
            server.save()

        app.host.add(server)

    return HttpResponse("Good")