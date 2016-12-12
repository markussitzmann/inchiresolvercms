# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 21:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20161212_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaLinkPlacement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_media_link_placements', to='home.HomePage')),
                ('social_media_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='home.SocialMediaLink')),
            ],
            options={
                'verbose_name': 'Social Media Link',
                'verbose_name_plural': 'Social Media Links',
            },
        ),
    ]
