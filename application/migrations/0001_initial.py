# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Owner'
        db.create_table('application_owner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('application', ['Owner'])

        # Adding model 'Importance'
        db.create_table('application_importance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('application', ['Importance'])

        # Adding model 'Application'
        db.create_table('application_application', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('applevel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['application.Importance'], null=True, blank=True)),
        ))
        db.send_create_signal('application', ['Application'])

        # Adding M2M table for field appowner on 'Application'
        db.create_table('application_application_appowner', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('application', models.ForeignKey(orm['application.application'], null=False)),
            ('owner', models.ForeignKey(orm['application.owner'], null=False))
        ))
        db.create_unique('application_application_appowner', ['application_id', 'owner_id'])

        # Adding M2M table for field host on 'Application'
        db.create_table('application_application_host', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('application', models.ForeignKey(orm['application.application'], null=False)),
            ('host', models.ForeignKey(orm['device.host'], null=False))
        ))
        db.create_unique('application_application_host', ['application_id', 'host_id'])


    def backwards(self, orm):
        
        # Deleting model 'Owner'
        db.delete_table('application_owner')

        # Deleting model 'Importance'
        db.delete_table('application_importance')

        # Deleting model 'Application'
        db.delete_table('application_application')

        # Removing M2M table for field appowner on 'Application'
        db.delete_table('application_application_appowner')

        # Removing M2M table for field host on 'Application'
        db.delete_table('application_application_host')


    models = {
        'application.application': {
            'Meta': {'object_name': 'Application'},
            'applevel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['application.Importance']", 'null': 'True', 'blank': 'True'}),
            'appowner': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['application.Owner']", 'symmetrical': 'False', 'blank': 'True'}),
            'host': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['device.Host']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'application.importance': {
            'Meta': {'object_name': 'Importance'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'application.owner': {
            'Meta': {'object_name': 'Owner'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
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

    complete_apps = ['application']
