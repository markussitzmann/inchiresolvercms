# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 18:58
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20170103_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='section_stream',
            field=wagtail.wagtailcore.fields.StreamField((('banner', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('heading_line2', wagtail.wagtailcore.blocks.CharBlock(required=False, verbose_name='Heading, second line')), ('abstract', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True))))), ('features', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('features', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(default='')), ('content', wagtail.wagtailcore.blocks.RichTextBlock()), ('icon', wagtail.wagtailcore.blocks.CharBlock(default='', verbose_name='Icon'))))))))))),
        ),
    ]
