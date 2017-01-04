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


class BannerBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True)
    heading_line2 = blocks.CharBlock(required=False, label="Heading, 2nd line")
    abstract = blocks.CharBlock(required=False)
    content = blocks.RichTextBlock(required=False)
    image = ImageChooserBlock(required=True)

    class Meta:
        icon = "placeholder"
        template = "home/banner_block.html"


class FeatureArticleBlock(blocks.StructBlock):
    heading = blocks.CharBlock(default="")
    content = blocks.RichTextBlock()
    icon = blocks.CharBlock(default="", label="Icon")

    class Meta:
        template = "home/feature_article_block.html"


class FeatureBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True)
    features = blocks.ListBlock(FeatureArticleBlock())

    class Meta:
        icon = "placeholder"
        template = "home/feature_block.html"
        form_template = "home/form.html"


class HomePage(Page):
    headertitle = models.CharField(max_length=255, verbose_name="Header Title")
    headersubtitle = models.CharField(max_length=255, blank=True, default="", verbose_name="Header Subtitle")
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    section_stream = StreamField([
        ('banner', BannerBlock()),
        ('features', FeatureBlock()),
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
        StreamFieldPanel('section_stream'),
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
