# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 20:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170228_1956'),
        ('blog', '0006_auto_20170228_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='header',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.EditorialHeader'),
        ),
    ]
