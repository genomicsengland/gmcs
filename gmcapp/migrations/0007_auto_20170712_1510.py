# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 15:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gmcapp', '0006_ods_ldp'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LdapGroup',
        ),
        migrations.RemoveField(
            model_name='ods',
            name='ldp',
        ),
        migrations.DeleteModel(
            name='Ods',
        ),
    ]