# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Host.level'
        db.delete_column('device_host', 'level_id')

        # Adding field 'Host.blah'
        db.add_column('device_host', 'blah', self.gf('django.db.models.fields.related.ForeignKey')(default=6, to=orm['device.Servicelevel']), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Host.level'
        db.add_column('device_host', 'level', self.gf('django.db.models.fields.related.ForeignKey')(default=6, to=orm['device.Servicelevel']), keep_default=False)

        # Deleting field 'Host.blah'
        db.delete_column('device_host', 'blah_id')


    models = {
        'device.function': {
            'Meta': {'object_name': 'Function'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'device.host': {
            'Meta': {'object_name': 'Host'},
            'blah': ('django.db.models.fields.related.ForeignKey', [], {'default': '6', 'to': "orm['device.Servicelevel']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ipaddress': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'serverfunction': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['device.Function']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'device.servicelevel': {
            'Meta': {'object_name': 'Servicelevel'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['device']
