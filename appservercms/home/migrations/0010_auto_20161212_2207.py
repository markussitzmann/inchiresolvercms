# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20161212_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='headersubtitle',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='headertitle',
            field=models.CharField(max_length=255),
        ),
    ]
