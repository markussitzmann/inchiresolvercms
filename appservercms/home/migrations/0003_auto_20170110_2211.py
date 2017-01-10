# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 22:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170110_2154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='editorialfeaturearticle',
            old_name='article_heading',
            new_name='heading',
        ),
        migrations.RenameField(
            model_name='editorialfeaturearticle',
            old_name='article_icon',
            new_name='icon',
        ),
        migrations.RenameField(
            model_name='editorialfeaturearticle',
            old_name='article_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='editorialpostarticle',
            old_name='article_heading',
            new_name='heading',
        ),
        migrations.RenameField(
            model_name='editorialpostarticle',
            old_name='article_icon',
            new_name='icon',
        ),
        migrations.RenameField(
            model_name='editorialpostarticle',
            old_name='article_image',
            new_name='post_image',
        ),
        migrations.RenameField(
            model_name='editorialpostarticle',
            old_name='article_text',
            new_name='text',
        ),
    ]