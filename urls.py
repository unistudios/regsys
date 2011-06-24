from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Testing ONLY!
    url(r'^$', direct_to_template, {'template':'index.html'} ),

    # Examples:
    # url(r'^$', 'regsys.views.home', name='home'),
    # url(r'^regsys/', include('regsys.foo.urls')),

    url(r'^device/', include('device.urls')),
#    url(r'^application/', include('application.urls')),
        
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )