# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adyengo', '0019_auto_20170303_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('amex', 'Amex'), ('bankTransfer', 'All banktransfers'), ('bankTransfer_DE', 'German Banktransfer'), ('bankTransfer_IBAN', 'International Bank Transfer (IBAN)'), ('bankTransfer_NL', 'Dutch Banktransfer'), ('bcmc', 'Bancontact card'), ('card', 'All debit and credit cards'), ('diners', 'Diners Club'), ('directEbanking', 'SofortUberweisung'), ('directdebit_NL', 'Direct Debit (Netherlands)'), ('discover', 'Discover'), ('dotpay', 'Dotpay'), ('ebanking_FI', 'Finnish E-Banking'), ('elv', 'ELV'), ('giropay', 'GiroPay'), ('ideal', 'iDEAL'), ('maestro', 'Maestro'), ('mc', 'Master Card'), ('paypal', 'PayPal'), ('sepadirectdebit', 'SEPA Direct Debit'), ('visa', 'Visa')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='recurringpaymentresult',
            name='result_code',
            field=models.CharField(choices=[('Authorised', 'Authorised'), ('Error', 'Error'), ('Received', 'Received'), ('Refused', 'Refused')], max_length=30),
        ),
        migrations.AlterField(
            model_name='session',
            name='country_code',
            field=models.CharField(choices=[('BE', 'Belgium'), ('DE', 'Germany'), ('GB', 'United Kingdom'), ('NL', 'Netherlands')], max_length=2),
        ),
        migrations.AlterField(
            model_name='session',
            name='page_type',
            field=models.CharField(choices=[('multiple', 'Multiple'), ('single', 'Single'), ('skip', 'Skip')], default='skip', max_length=15),
        ),
        migrations.AlterField(
            model_name='session',
            name='recurring_contract',
            field=models.CharField(blank=True, choices=[('ONECLICK', 'One click'), ('RECURRING', 'Recurring'), ('RECURRING,ONECLICK', 'Recurring and One click (user chooses)')], max_length=50),
        ),
        migrations.AlterField(
            model_name='session',
            name='shopper_locale',
            field=models.CharField(blank=True, choices=[('de_DE', 'German (Germany)'), ('en_GB', 'English (United Kingdom)'), ('fr_BE', 'French (Belgium)'), ('nl_BE', 'Dutch (Belgium)'), ('nl_NL', 'Dutch (Holland)')], default='nl_NL', max_length=5),
        ),
        migrations.AlterField(
            model_name='sessionallowedpaymentmethods',
            name='method',
            field=models.CharField(choices=[('amex', 'Amex'), ('bankTransfer', 'All banktransfers'), ('bankTransfer_DE', 'German Banktransfer'), ('bankTransfer_IBAN', 'International Bank Transfer (IBAN)'), ('bankTransfer_NL', 'Dutch Banktransfer'), ('bcmc', 'Bancontact card'), ('card', 'All debit and credit cards'), ('diners', 'Diners Club'), ('directEbanking', 'SofortUberweisung'), ('directdebit_NL', 'Direct Debit (Netherlands)'), ('discover', 'Discover'), ('dotpay', 'Dotpay'), ('ebanking_FI', 'Finnish E-Banking'), ('elv', 'ELV'), ('giropay', 'GiroPay'), ('ideal', 'iDEAL'), ('maestro', 'Maestro'), ('mc', 'Master Card'), ('paypal', 'PayPal'), ('sepadirectdebit', 'SEPA Direct Debit'), ('visa', 'Visa')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sessionblockedpaymentmethods',
            name='method',
            field=models.CharField(choices=[('amex', 'Amex'), ('bankTransfer', 'All banktransfers'), ('bankTransfer_DE', 'German Banktransfer'), ('bankTransfer_IBAN', 'International Bank Transfer (IBAN)'), ('bankTransfer_NL', 'Dutch Banktransfer'), ('bcmc', 'Bancontact card'), ('card', 'All debit and credit cards'), ('diners', 'Diners Club'), ('directEbanking', 'SofortUberweisung'), ('directdebit_NL', 'Direct Debit (Netherlands)'), ('discover', 'Discover'), ('dotpay', 'Dotpay'), ('ebanking_FI', 'Finnish E-Banking'), ('elv', 'ELV'), ('giropay', 'GiroPay'), ('ideal', 'iDEAL'), ('maestro', 'Maestro'), ('mc', 'Master Card'), ('paypal', 'PayPal'), ('sepadirectdebit', 'SEPA Direct Debit'), ('visa', 'Visa')], max_length=50),
        ),
    ]
