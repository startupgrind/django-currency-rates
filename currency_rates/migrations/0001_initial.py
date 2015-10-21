# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Currency'
        db.create_table('currency_rates_currency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('symbol', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('is_default', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('currency_rates', ['Currency'])

        # Adding model 'ExchangeRate'
        db.create_table('currency_rates_exchangerate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rates', to=orm['currency_rates.Currency'])),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('rate', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=6)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('currency_rates', ['ExchangeRate'])

        # Adding unique constraint on 'ExchangeRate', fields ['currency', 'date']
        db.create_unique('currency_rates_exchangerate', ['currency_id', 'date'])


    def backwards(self, orm):
        # Removing unique constraint on 'ExchangeRate', fields ['currency', 'date']
        db.delete_unique('currency_rates_exchangerate', ['currency_id', 'date'])

        # Deleting model 'Currency'
        db.delete_table('currency_rates_currency')

        # Deleting model 'ExchangeRate'
        db.delete_table('currency_rates_exchangerate')


    models = {
        'currency_rates.currency': {
            'Meta': {'ordering': "('code',)", 'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'})
        },
        'currency_rates.exchangerate': {
            'Meta': {'ordering': "('-date', 'currency__code')", 'unique_together': "(('currency', 'date'),)", 'object_name': 'ExchangeRate'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rates'", 'to': "orm['currency_rates.Currency']"}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'})
        }
    }

    complete_apps = ['currency_rates']