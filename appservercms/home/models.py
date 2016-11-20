from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock


class HomePage(Page):
    pass


class TileBlock(blocks.StructBlock):
    style = blocks.ChoiceBlock(choices=[
        ('style1', 'Style1'),
        ('style2', 'Style2'),
        ('style3', 'Style3'),
        ('style4', 'Style4'),
        ('style5', 'Style5'),
    ])
    heading = blocks.CharBlock(required=True)
    content = blocks.RichTextBlock()
    image = ImageChooserBlock(required=True)
    url = blocks.URLBlock()

    class Meta:
        icon = "placeholder"
        template = "stream/tile_block.html"


class StreamPage(Page):
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    main = StreamField([
        ('tile', TileBlock())
    ])

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        StreamFieldPanel('main'),
    ]
