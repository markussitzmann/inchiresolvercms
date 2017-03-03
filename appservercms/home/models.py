from __future__ import absolute_import, unicode_literals

from django.db import models
from django.db.models import CharField, URLField, BooleanField
from django.db.models import ForeignKey
from django.utils.encoding import python_2_unicode_compatible
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.wagtailcore.blocks import CharBlock, RichTextBlock, StructBlock, ChoiceBlock, ListBlock, StreamBlock
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet


class GenericImageBlock(StructBlock):
    template_type = ChoiceBlock(
        choices=[
            ('main', 'Main'),
            ('fit', 'Fit'),
            ('left', 'Left'),
            ('right', 'Right'),
        ]
    )
    wagtail_resize = CharBlock(max_length=25)
    image = ImageChooserBlock()

    class Meta:
        template = "home/generic_image_block.html"
        icon = 'image'


class GenericColumnBlock:
    stream_block_blocks = [
        ('text', RichTextBlock()),
        ('image', GenericImageBlock())
    ]

class GenericDoubleColumnBlock(StructBlock, GenericColumnBlock):
    column1 = StreamBlock(GenericColumnBlock.stream_block_blocks)
    column2 = StreamBlock(GenericColumnBlock.stream_block_blocks)

    class Meta:
        template = "home/generic_double_column_block.html"


class GenericTripleColumnBlock(StructBlock, GenericColumnBlock):
    column1 = StreamBlock(GenericColumnBlock.stream_block_blocks)
    column2 = StreamBlock(GenericColumnBlock.stream_block_blocks)
    column3 = StreamBlock(GenericColumnBlock.stream_block_blocks)

    class Meta:
        template = "home/generic_triple_column_block.html"


class EditorialPage(Page):
    header = models.ForeignKey('home.EditorialHeader',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')
    banner_display = BooleanField(default=False)
    banner_heading = CharField(max_length=255, blank=True, default="")
    banner_heading_line2 = CharField(max_length=255, blank="True", default="", verbose_name="Heading, 2nd line")
    banner_abstract = CharField(max_length=4096, blank="True", default="")
    banner_text = RichTextField(blank="True")
    banner_image = models.ForeignKey('wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')
    banner_button = models.ForeignKey('home.EditorialActionButton',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')
    feature_display = BooleanField(default=False)
    feature_heading = CharField(max_length=255, blank=True, default="")
    # features per relationship
    post_display = BooleanField(default=False)
    post_heading = CharField(max_length=255, blank=True, default="")
    # post per relationship
    generic_display = BooleanField(default=False)
    generic_headline = CharField(max_length=255, blank=True, default="")
    generic_content = StreamField([
        ('heading', CharBlock(classname="full title")),
        ('paragraph', RichTextBlock()),
        ('image', GenericImageBlock()),
        ('table', TableBlock()),
        ('double_column', GenericDoubleColumnBlock()),
        ('triple_column', GenericTripleColumnBlock()),
    ], blank=True, default="")

    search_fields = Page.search_fields + [
        index.SearchField('banner_heading'),
        index.SearchField('banner_heading_line2'),
        index.SearchField('banner_abstract'),
        index.SearchField('banner_text'),

        index.SearchField('feature_display'),
        index.SearchField('feature_heading'),
        index.RelatedFields('feature_articles', [
            index.SearchField('heading'),
            index.SearchField('text'),
        ]),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                SnippetChooserPanel('header'),
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
                SnippetChooserPanel('banner_button')
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
            ],
            heading="Posts",
        ),
        MultiFieldPanel(
            [
                FieldPanel('generic_display'),
                FieldPanel('generic_headline'),
                StreamFieldPanel('generic_content'),
            ],
            heading="Generic",
        ),
    ]


class Article(models.Model):
    heading = CharField(max_length=255, blank=True, default="")
    text = RichTextField(blank="True")
    icon = CharField(max_length=25, blank="True", default="")

    class Meta:
        abstract = True


@register_snippet
@python_2_unicode_compatible
class EditorialHeader(ClusterableModel, models.Model):
    title = CharField(max_length=255)
    subtitle = CharField(max_length=255)
    url = URLField(blank=True, default="")

    panels = [
        FieldPanel('title'),
        FieldPanel('subtitle'),
        FieldPanel('url'),
        InlinePanel('header_social_media_link_placements', label="Social Media Links")
    ]

    def __str__(self):
        r = self.title + " (" + self.subtitle + ")"
        return r


class EditorialFeatureArticle(Orderable, Article):
    page = ParentalKey('home.EditorialPage', related_name='feature_articles')
    button = models.ForeignKey('home.EditorialActionButton',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')

    panels = [
        FieldPanel('heading'),
        FieldPanel('text'),
        FieldPanel('icon'),
        SnippetChooserPanel('button')
    ]


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


class EditorialHeaderSocialMediaLinkPlacement(Orderable, models.Model):
    parent = ParentalKey('home.EditorialHeader', related_name='header_social_media_link_placements')
    social_media_link = ForeignKey(
        'EditorialSocialMediaLink',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='header_social_media_link_placement')

    panels = [
        SnippetChooserPanel('social_media_link')
    ]

    def __str__(self):
        return self.page.title + " -> " + self.social_media_link.name


class EditorialSocialMediaLinkPlacement(Orderable, models.Model):
    page = ParentalKey('EditorialPage', related_name='social_media_link_placements')
    social_media_link = ForeignKey(
        'EditorialSocialMediaLink',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='social_media_link_placement')

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
    url = URLField(default="")
    size = CharField(max_length=25, choices=SIZE_CHOICES, blank=True, default="")
    icon = CharField(max_length=25, blank=True, default="")

    panels = [
        FieldPanel('name'),
        FieldPanel('size'),
        FieldPanel('url'),
        FieldPanel('icon'),
    ]

    def __str__(self):
        r = self.name + " (" + self.url + ")"
        if self.size:
            r = r + ", " + self.size
        return r



