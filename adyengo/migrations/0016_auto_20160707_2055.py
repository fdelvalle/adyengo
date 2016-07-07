# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-07 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adyengo', '0015_auto_20160707_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('bankTransfer_DE', 'German Banktransfer'), ('elv', 'ELV'), ('paypal', 'PayPal'), ('amex', 'Amex'), ('mc', 'Master Card'), ('bankTransfer_NL', 'Dutch Banktransfer'), ('ideal', 'iDEAL'), ('directEbanking', 'SofortUberweisung'), ('card', 'All debit and credit cards'), ('bankTransfer', 'All banktransfers'), ('visa', 'Visa'), ('directdebit_NL', 'Direct Debit (Netherlands)')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='recurringpaymentresult',
            name='result_code',
            field=models.CharField(choices=[('Refused', 'Refused'), ('Error', 'Error'), ('Received', 'Received'), ('Authorised', 'Authorised')], max_length=30),
        ),
        migrations.AlterField(
            model_name='session',
            name='country_code',
            field=models.CharField(choices=[('DE', 'Germany'), ('GB', 'United Kingdom'), ('NL', 'Netherlands'), ('BE', 'Belgium')], max_length=2),
        ),
        migrations.AlterField(
            model_name='session',
            name='page_type',
            field=models.CharField(choices=[('multiple', 'Multiple'), ('single', 'Single'), ('skip', 'Skip')], default='multiple', max_length=15),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_type',
            field=models.CharField(choices=[('hpp_recurring', 'HPP Recurring'), ('api_recurring', 'API Recurring'), ('hpp_regular', 'HPP Regular')], max_length=25),
        ),
        migrations.AlterField(
            model_name='session',
            name='shopper_locale',
            field=models.CharField(blank=True, choices=[('nl_BE', 'Dutch (Belgium)'), ('nl_NL', 'Dutch (Holland)'), ('de_DE', 'German (Germany)'), ('en_GB', 'English (United Kingdom)'), ('fr_BE', 'French (Belgium)')], default='nl_NL', max_length=5),
        ),
        migrations.AlterField(
            model_name='sessionallowedpaymentmethods',
            name='method',
            field=models.CharField(choices=[('bankTransfer_DE', 'German Banktransfer'), ('elv', 'ELV'), ('paypal', 'PayPal'), ('amex', 'Amex'), ('mc', 'Master Card'), ('bankTransfer_NL', 'Dutch Banktransfer'), ('ideal', 'iDEAL'), ('directEbanking', 'SofortUberweisung'), ('card', 'All debit and credit cards'), ('bankTransfer', 'All banktransfers'), ('visa', 'Visa'), ('directdebit_NL', 'Direct Debit (Netherlands)')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sessionblockedpaymentmethods',
            name='method',
            field=models.CharField(choices=[('bankTransfer_DE', 'German Banktransfer'), ('elv', 'ELV'), ('paypal', 'PayPal'), ('amex', 'Amex'), ('mc', 'Master Card'), ('bankTransfer_NL', 'Dutch Banktransfer'), ('ideal', 'iDEAL'), ('directEbanking', 'SofortUberweisung'), ('card', 'All debit and credit cards'), ('bankTransfer', 'All banktransfers'), ('visa', 'Visa'), ('directdebit_NL', 'Direct Debit (Netherlands)')], max_length=50),
        ),
    ]
