from __future__ import absolute_import, unicode_literals

from django.db import models
from django.db.models import CharField, DateField, URLField, BooleanField
from django.db.models import ForeignKey
from django.utils.encoding import python_2_unicode_compatible
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import ListBlock
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet


class EditorialPage(Page):
    header_title = CharField(max_length=255, verbose_name="Heading")
    header_subtitle = CharField(max_length=255, blank=True, default="", verbose_name="Subtitle")
    banner_display = BooleanField(default=True)
    banner_heading = CharField(max_length=255, blank=True, default="")
    banner_heading_line2 = CharField(max_length=255, blank="True", default="", verbose_name="Headling, 2nd line")
    banner_abstract = CharField(max_length=4096, blank="True", default="")
    banner_text = RichTextField(blank="True")
    banner_image = models.ForeignKey('wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')
    feature_display = BooleanField(default=True)
    feature_heading = CharField(max_length=255, blank=True, default="")
    # features per relationship
    post_display = BooleanField(default=True)
    post_heading = CharField(max_length=255, blank=True, default="")
    # post per relationship
    author = CharField(max_length=255)
    date = DateField("Post date")

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('header_title'),
                FieldPanel('header_subtitle'),
                InlinePanel('social_media_link_placements', label="Social Media Links"),
            ],
            heading="Header",
        ),
        MultiFieldPanel(
            [
                FieldPanel('banner_display'),
                FieldPanel('banner_heading'),
                FieldPanel('banner_heading_line2'),
                FieldPanel('banner_abstract'),
                FieldPanel('banner_text'),
                ImageChooserPanel('banner_image'),
                InlinePanel('action_button_placements', label="Buttons")
            ],
            heading="Banner",
        ),
        MultiFieldPanel(
            [
                FieldPanel('feature_display'),
                FieldPanel('feature_heading'),
                InlinePanel('feature_articles', label="Feature Articles")
            ],
            heading="Features",
        ),
        MultiFieldPanel(
            [
                FieldPanel('post_display'),
                FieldPanel('post_heading'),
                InlinePanel('post_articles', label="Post Articles"),
                InlinePanel('action_button_placements', label="Buttons")
            ],
            heading="Posts",
        ),
        MultiFieldPanel(
            [
                FieldPanel('author'),
                FieldPanel('date')
            ],
            heading="Meta",
        )
    ]


class Article(models.Model):
    heading = CharField(max_length=255, blank=True, default="")
    text = RichTextField(blank="True")
    icon = CharField(max_length=25, blank="True", default="")

    class Meta:
        abstract = True


class EditorialFeatureArticle(Orderable, Article):
    page = ParentalKey('home.EditorialPage', related_name='feature_articles')


class EditorialPostArticle(Orderable, Article):
    page = ParentalKey('home.EditorialPage', related_name='post_articles')
    image = models.ForeignKey('wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')
    button = models.ForeignKey('home.EditorialActionButton',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')

    panels = [
        FieldPanel('heading'),
        FieldPanel('text'),
        ImageChooserPanel('image'),
        SnippetChooserPanel('button')
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


@register_snippet
@python_2_unicode_compatible
class EditorialActionButton(models.Model):
    SIZE_CHOICES = (
        ('', 'Default'),
        ('small', 'Small'),
        ('big', 'Big'),
    )

    name = CharField(max_length=255)
    size = CharField(max_length=25, choices=SIZE_CHOICES, blank=True, default="")
    icon = CharField(max_length=25)
    url = URLField()

    panels = [
        FieldPanel('name'),
        FieldPanel('size'),
        FieldPanel('url'),
        FieldPanel('icon'),
    ]

    def __str__(self):
        return self.name


class EditorialActionButtonPlacement(Orderable, models.Model):
    page = ParentalKey('EditorialPage', related_name='action_button_placements')
    action_button = ForeignKey(
        'EditorialActionButton',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')

    panels = [
        SnippetChooserPanel('action_button')
    ]

    def __str__(self):
        return self.page.title + " -> " + self.action_button.name
