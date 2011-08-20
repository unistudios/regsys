from django.core.exceptions import ObjectDoesNotExist
from device.models import *
from application.models import *
import csv
import sys

if sys.argv[1]:
    f = csv.reader(open(sys.argv[1]))

for l in f:
    servername = l[0]
    appname    = l[1]

    print l,
    
    try:
        server  = Host.objects.get(name=servername)
    except ObjectDoesNotExist:
        print "Adding",
        server = Host(name=servername)
        server.save()
    except:
        continue 

    if appname:
        # add if necessary
        try:
            app = Application.objects.get(name=appname)
        except ObjectDoesNotExist:
            print "Adding app %s" % appname,
            app = Application(name=appname)
            app.save()
        except:
            continue
         
        app.host.add(server)
    print