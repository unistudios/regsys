# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Servicelevel'
        db.create_table('device_servicelevel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('device', ['Servicelevel'])

        # Adding model 'Function'
        db.create_table('device_function', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('device', ['Function'])

        # Adding model 'OperatingSystem'
        db.create_table('device_operatingsystem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('device', ['OperatingSystem'])

        # Adding model 'Host'
        db.create_table('device_host', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ipaddress', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True, blank=True)),
            ('serverlevel', self.gf('django.db.models.fields.related.ForeignKey')(default=6, to=orm['device.Servicelevel'])),
            ('OS', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['device.OperatingSystem'])),
        ))
        db.send_create_signal('device', ['Host'])

        # Adding M2M table for field serverfunction on 'Host'
        db.create_table('device_host_serverfunction', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('host', models.ForeignKey(orm['device.host'], null=False)),
            ('function', models.ForeignKey(orm['device.function'], null=False))
        ))
        db.create_unique('device_host_serverfunction', ['host_id', 'function_id'])


    def backwards(self, orm):
        
        # Deleting model 'Servicelevel'
        db.delete_table('device_servicelevel')

        # Deleting model 'Function'
        db.delete_table('device_function')

        # Deleting model 'OperatingSystem'
        db.delete_table('device_operatingsystem')

        # Deleting model 'Host'
        db.delete_table('device_host')

        # Removing M2M table for field serverfunction on 'Host'
        db.delete_table('device_host_serverfunction')


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
            'ipaddress': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
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
