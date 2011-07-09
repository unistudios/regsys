from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'device.views.index'),
    (r'^data/$', 'device.views.data'), 
)