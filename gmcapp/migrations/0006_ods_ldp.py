# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 21:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gmcapp', '0005_auto_20170711_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='ods',
            name='ldp',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gmcapp.Ldp'),
            preserve_default=False,
        ),
    ]
