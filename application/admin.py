from application.models import Application,Owner,Importance

from django.contrib import admin


""" 
ApplicationAdmin - Shows which servers are attached. 
"""
class ApplicationAdmin(admin.ModelAdmin):
    fields = ('name', 'applevel', 'appowner','adminHostList')
#    fields = ('name', 'applevel', 'appowner',)
    readonly_fields = ['adminHostList']
    search_fields = ['name', ]
    
admin.site.register(Application, ApplicationAdmin)


admin.site.register(Owner)
admin.site.register(Importance)
