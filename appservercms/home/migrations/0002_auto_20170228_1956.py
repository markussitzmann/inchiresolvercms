# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 19:56
from __future__ import unicode_literals

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editorialpage',
            name='generic_content',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('template_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('main', 'Main'), ('fit', 'Fit'), ('left', 'Left'), ('right', 'Right')])), ('wagtail_resize', wagtail.wagtailcore.blocks.CharBlock(max_length=25)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())))), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('double_column', wagtail.wagtailcore.blocks.StructBlock((('column1', wagtail.wagtailcore.blocks.StreamBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('template_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('main', 'Main'), ('fit', 'Fit'), ('left', 'Left'), ('right', 'Right')])), ('wagtail_resize', wagtail.wagtailcore.blocks.CharBlock(max_length=25)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()))))))), ('column2', wagtail.wagtailcore.blocks.StreamBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('template_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('main', 'Main'), ('fit', 'Fit'), ('left', 'Left'), ('right', 'Right')])), ('wagtail_resize', wagtail.wagtailcore.blocks.CharBlock(max_length=25)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())))))))))), ('triple_column', wagtail.wagtailcore.blocks.StructBlock((('column1', wagtail.wagtailcore.blocks.StreamBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('template_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('main', 'Main'), ('fit', 'Fit'), ('left', 'Left'), ('right', 'Right')])), ('wagtail_resize', wagtail.wagtailcore.blocks.CharBlock(max_length=25)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()))))))), ('column2', wagtail.wagtailcore.blocks.StreamBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('template_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('main', 'Main'), ('fit', 'Fit'), ('left', 'Left'), ('right', 'Right')])), ('wagtail_resize', wagtail.wagtailcore.blocks.CharBlock(max_length=25)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()))))))), ('column3', wagtail.wagtailcore.blocks.StreamBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('template_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('main', 'Main'), ('fit', 'Fit'), ('left', 'Left'), ('right', 'Right')])), ('wagtail_resize', wagtail.wagtailcore.blocks.CharBlock(max_length=25)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()))))))))))), blank=True, default=''),
        ),
    ]