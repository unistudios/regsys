from device.models import Host, Servicelevel, Function, OperatingSystem
from django.contrib import admin

admin.site.register(Host)
admin.site.register(Servicelevel)
admin.site.register(Function)
admin.site.register(OperatingSystem)