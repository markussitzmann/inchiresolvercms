# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 21:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0016_deprecate_rendition_filter_relation'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditorialPostArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('article_heading', models.CharField(blank=True, default='', max_length=255)),
                ('article_text', wagtail.wagtailcore.fields.RichTextField(blank='True')),
                ('article_icon', models.CharField(blank='True', default='', max_length=25)),
                ('article_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
        migrations.RenameField(
            model_name='editorialfeaturearticle',
            old_name='feature_article_heading',
            new_name='article_heading',
        ),
        migrations.RenameField(
            model_name='editorialfeaturearticle',
            old_name='feature_icon',
            new_name='article_icon',
        ),
        migrations.RenameField(
            model_name='editorialfeaturearticle',
            old_name='feature_text',
            new_name='article_text',
        ),
        migrations.AddField(
            model_name='editorialpage',
            name='post_display',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='editorialpage',
            name='post_heading',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='editorialpostarticle',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_articles', to='home.EditorialPage'),
        ),
    ]