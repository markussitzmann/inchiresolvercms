# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 22:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20170110_2211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='editorialpostarticle',
            old_name='post_image',
            new_name='image',
        ),
    ]