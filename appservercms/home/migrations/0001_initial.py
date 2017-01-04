# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 13:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('headertitle', models.CharField(max_length=255, verbose_name='Header Title')),
                ('headersubtitle', models.CharField(blank=True, default='', max_length=255, verbose_name='Header Subtitle')),
                ('author', models.CharField(max_length=255)),
                ('date', models.DateField(verbose_name='Post date')),
                ('section_stream', wagtail.wagtailcore.fields.StreamField((('banner', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('headingline2', wagtail.wagtailcore.blocks.CharBlock()), ('headingtext', wagtail.wagtailcore.blocks.CharBlock()), ('content', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True))))), ('features', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('features', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((), content=wagtail.wagtailcore.blocks.RichTextBlock(), heading=wagtail.wagtailcore.blocks.CharBlock(default=''), icon=models.CharField(blank=True, default='', max_length=25)))))))), default='')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SocialMediaLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.CharField(choices=[('fa-linkedin', 'fa-linkedin'), ('fa-facebook', 'fa-facebook'), ('fa-twitter', 'fa-twitter'), ('fa-instagram', 'fa-instagram'), ('fa-medium', 'fa-medium')], default='linkedin', max_length=25)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Social Media Links',
                'verbose_name': 'Social Media Link',
            },
        ),
        migrations.CreateModel(
            name='SocialMediaLinkPlacement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_media_link_placements', to='home.HomePage')),
                ('social_media_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.SocialMediaLink')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
    ]
