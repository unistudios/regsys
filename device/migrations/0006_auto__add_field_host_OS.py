# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Host.OS'
        db.add_column('device_host', 'OS', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['device.OperatingSystem']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Host.OS'
        db.delete_column('device_host', 'OS_id')


    models = {
        'device.function': {
            'Meta': {'object_name': 'Function'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'device.host': {
            'Meta': {'object_name': 'Host'},
            'OS': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['device.OperatingSystem']"}),
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
