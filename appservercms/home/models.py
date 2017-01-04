from __future__ import absolute_import, unicode_literals

from django.db import models
from django.db.models import CharField, DateField, URLField
from django.db.models import ForeignKey
from django.utils.encoding import python_2_unicode_compatible
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet





# class FeatureArticleBlock(blocks.StructBlock):
#     heading = blocks.CharBlock(default="")
#     content = blocks.RichTextBlock()
#     icon = blocks.CharBlock(default="", label="Icon")
#
#     class Meta:
#         template = "home/feature_article_block.html"


# class FeatureBlock(blocks.StructBlock):
#     heading = blocks.CharBlock(required=True)
#     features = blocks.ListBlock(FeatureArticleBlock())
#
#     class Meta:
#         icon = "placeholder"
#         template = "home/feature_block.html"
#         form_template = "home/form.html"


class EditorialPage(Page):
    headertitle = CharField(max_length=255, verbose_name="Heading")
    headersubtitle = CharField(max_length=255, blank=True, default="", verbose_name="Subtitle")
    author = CharField(max_length=255)
    date = DateField("Post date")
    # section_stream = StreamField([
    #     ('banner', BannerBlock()),
    #     ('features', FeatureBlock()),
    # ])

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('headertitle'),
                FieldPanel('headersubtitle'),
                InlinePanel('social_media_link_placements', label="Social Media Links"),
            ],
            heading="Header",
        ),
        InlinePanel('banners', label="Banners"),
        FieldPanel('author'),
        FieldPanel('date')

        # StreamFieldPanel('section_stream'),
    ]


class EditorialPageBanner(Orderable):
    page = ParentalKey('EditorialPage', related_name='banners')
    heading = CharField(max_length=255)
    heading_line2 = CharField(max_length=255, blank="True", verbose_name="Headling, 2nd line")
    abstract = CharField(max_length=4096, blank="True")
    content = RichTextField(blank="True")
    image = models.ForeignKey('wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('heading'),
        FieldPanel('heading_line2'),
        FieldPanel('abstract'),
        FieldPanel('content'),
        ImageChooserPanel('image')
    ]


@register_snippet
@python_2_unicode_compatible
class EditorialSocialMediaLink(models.Model):
    ICON_CHOICES = (
        ('fa-linkedin', 'fa-linkedin'),
        ('fa-facebook', 'fa-facebook'),
        ('fa-twitter', 'fa-twitter'),
        ('fa-instagram', 'fa-instagram'),
        ('fa-medium', 'fa-medium')
    )
    name = CharField(max_length=255)
    icon = CharField(max_length=25, choices=ICON_CHOICES, default="linkedin")
    url = URLField()

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


class EditorialSocialMediaLinkPlacement(Orderable, models.Model):
    page = ParentalKey('EditorialPage', related_name='social_media_link_placements')
    social_media_link = ForeignKey(
        'EditorialSocialMediaLink',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')

    panels = [
        SnippetChooserPanel('social_media_link')
    ]

    def __str__(self):
        return self.page.title + " -> " + self.social_media_link.name


# @register_snippet
# @python_2_unicode_compatible
# class ActionButton(models.Model):
#     SIZE_CHOICES = (
#         ('', 'Default'),
#         ('small', 'Small'),
#         ('big', 'Big'),
#     )
#
#     name = CharField(max_length=255)
#     size = CharField(max_length=25, choices=SIZE_CHOICES, default="")
#     icon = CharField(max_length=25)
#     url = URLField()
#
#     panels = [
#         SnippetChooserPanel('Action Button')
#     ]
#
#     def __str__(self):
#         return self.name