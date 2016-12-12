from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet


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
        template = "home/tile_block.html"


class BannerSectionBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True)
    headingline2 = blocks.CharBlock()
    headingtext = blocks.CharBlock()
    content = blocks.RichTextBlock()
    image = ImageChooserBlock(required=True)

    class Meta:
        icon = "placeholder"
        template = "home/banner_section_block.html"


class HomePage(Page):
    headertitle = models.CharField(max_length=255, verbose_name="Header Title")
    headersubtitle = models.CharField(max_length=255, blank=True, default="", verbose_name="Header Subtitle")
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    sectionstream = StreamField([
        ('banner', BannerSectionBlock())
    ])

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('headertitle'),
                FieldPanel('headersubtitle'),
                InlinePanel('social_media_link_placements', label="Social Media Links"),
            ],
            heading="Header",
        ),
        FieldPanel('author'),
        FieldPanel('date'),
        StreamFieldPanel('sectionstream'),
    ]


@register_snippet
@python_2_unicode_compatible
class SocialMediaLink(models.Model):
    ICON_CHOICES = (
        ('fa-linkedin', 'fa-linkedin'),
        ('fa-facebook', 'fa-facebook'),
        ('fa-twitter', 'fa-twitter'),
        ('fa-instagram', 'fa-instagram'),
        ('fa-medium', 'fa-medium')
    )
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=25, choices=ICON_CHOICES, default="linkedin")
    url = models.URLField()

    class Meta:
        verbose_name = "Social Media Link"
        verbose_name_plural = "Social Media Links"

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
        FieldPanel('icon'),
    ]

    def __str__(self):
        return self.name


class SocialMediaLinkPlacement(Orderable, models.Model):
    page = ParentalKey('HomePage', related_name='social_media_link_placements')
    social_media_link = models.ForeignKey(
        'SocialMediaLink',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')

    panels = [
        SnippetChooserPanel('social_media_link')
    ]

    def __str__(self):
        return self.page.title + " -> " + self.social_media_link.name
