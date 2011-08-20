# Create your views here.
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from device.models import Host
from application.models import Application

def index(request):
    return HttpResponse("Not done yet")

def update(request):
    if request.method == 'POST':
        # try to get all our varialbes
        try:
            servername  = request.POST['servername'].lower()

            try:
                server  = Host.objects.get(name=servername)
            except ObjectDoesNotExist:
                print "Adding Server"
                server = Host(name=servername)
                server.save()
            except:
                return HttpResponse("Error on Servername" )

        except KeyError:
            return HttpResponse("Didn't provide a servername")

        try:
            appname = request.POST['appname'].capitalize()

            # add if necessary
            try:
                app = Application.objects.get(name=appname)
            except ObjectDoesNotExist:
                app = Application(name=appname)
                app.save()
                app.host.add(server)
            except:
                return HttpResponse("Error setting up app")
                
        except:
            #no appname specified, that's OK.
            pass

    return HttpResponse("Server ID = %s" % str(server.id) )