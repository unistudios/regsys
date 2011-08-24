# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'OperatingSystem'
        db.create_table('device_operatingsystem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('device', ['OperatingSystem'])


    def backwards(self, orm):
        
        # Deleting model 'OperatingSystem'
        db.delete_table('device_operatingsystem')


    models = {
        'device.function': {
            'Meta': {'object_name': 'Function'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'device.host': {
            'Meta': {'object_name': 'Host'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ipaddress': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'serverfunction': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['device.Function']", 'symmetrical': 'False', 'blank': 'True'}),
            'serverlevel': ('django.db.models.fields.related.ForeignKey', [], {'default': '6', 'to': "orm['device.Servicelevel']"})
        },
        'device.operatingsystem': {
            'Meta': {'object_name': 'OperatingSystem'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'device.servicelevel': {
            'Meta': {'object_name': 'Servicelevel'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['device']
