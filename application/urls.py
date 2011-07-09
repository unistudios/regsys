from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'application.views.index'),

    (r'^update/$', 'application.views.update'),
)