# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import itertools
from django.forms import widgets
from django.core.exceptions import ValidationError
from django.utils.html import format_html, format_html_join, escape, mark_safe
from django.utils.encoding import force_text
from django.utils.translation import ungettext_lazy, ugettext_lazy as _
from django.forms.models import ModelForm
from django.forms.fields import ChoiceField
from django.forms.fields import IntegerField
from cms.plugin_pool import plugin_pool
from cmsplugin_cascade.widgets import NumberInputWidget
from cmsplugin_cascade.forms import ManageChildrenFormMixin
from cmsplugin_cascade.fields import PartialFormField
from cmsplugin_cascade.generic.cms_plugins import HeadingPlugin
from cmsplugin_cascade.mixins import TransparentMixin
from cmsplugin_cascade.link.cms_plugins import TextLinkPlugin
#from cmsplugin_filer_image.cms_plugins import FilerImagePlugin
#from filer.fields.image import AdminImageWidget


#from djangocms_text_ckeditor.cms_plugins import TextPlugin
from djangocms_text_ckeditor.widgets import TextEditorWidget
from .plugin_base import Html5UpPluginBase
#from .settings import cascade_config


# class Html5UpImagePlugin(FilerImagePlugin, Html5UpPluginBase):
#     name = _("Html5Up Image Plugin")
#     #parent_classes = ('Html5UpSpotlightPlugin',)
#     require_parent = True
#     allow_children = False
#     render_template = 'html5up_image.html'
#     fieldsets = (
#         (None, {
#             'fields': [
#                 'caption_text',
#                 ('image', 'image_url',),
#                 'alt_text',
#             ]
#         }),
#         (_('Image resizing options'), {
#             'fields': (
#                 'use_original_image',
#                 ('width', 'height', 'crop', 'upscale'),
#                 'thumbnail_option',
#                 'use_autoscale',
#             )
#         }),
#         (None, {
#             'fields': ('alignment',)
#         }),
#         (_('More'), {
#             'classes': ('collapse',),
#             'fields': (('free_link', 'page_link', 'file_link', 'original_link', 'target_blank'), 'description',)
#         }),
#     )

#plugin_pool.register_plugin(Html5UpImagePlugin)


class Html5UpTextPlugin(Html5UpPluginBase):
    name = _("Html5Up Text")
    require_parent = True
    allow_children = False
    render_template = 'html5up_abstract_text.html'
    glossary_fields = (
        PartialFormField('abstract', TextEditorWidget(),),
    )

    @classmethod
    def get_identifier(cls, instance):
        # identifier = super(HtmlFiveUpContainerPlugin, cls).get_identifier(instance)
        identifier = "Html5Up Text"
        return identifier

    def render(self, context, instance, placeholder):
        abstract = instance.glossary.get('abstract', '')
        context.update({
            'abstract': Html5UpTextPlugin.unescape_html(abstract),
        })
        return super(Html5UpTextPlugin, self).render(context, instance, placeholder)

plugin_pool.register_plugin(Html5UpTextPlugin)



class Html5UpActionLinksForm(ManageChildrenFormMixin, ModelForm):
    num_children = IntegerField(min_value=1, initial=1,
        widget=NumberInputWidget(attrs={'size': '3', 'style': 'width: 5em !important;'}),
        label=_("Action Links"),
        help_text=_("Number of action links"))


class Html5UpActionLinksPlugin(Html5UpPluginBase):
    name = _("Action Links")
    form = Html5UpActionLinksForm
    parent_classes = ('Html5UpFullScreenPlugin', 'Html5UpSpotlightPlugin', 'Html5UpSectionPlugin')
    require_parent = True
    allow_children = True
    child_classes = None
    render_template = 'html5up_action_link_plugin.template'


    @classmethod
    def get_identifier(cls, instance):
        identifier = super(Html5UpActionLinksPlugin, cls).get_identifier(instance)
        num_cols = instance.get_children().count()
        content = ungettext_lazy('with {} link', 'with {} links', num_cols).format(num_cols)
        return format_html('{0}{1}', identifier, content)

    def save_model(self, request, obj, form, change):
        wanted_children = int(form.cleaned_data.get('num_children'))
        super(Html5UpActionLinksPlugin, self).save_model(request, obj, form, change)
        self.extend_children(obj, wanted_children, TextLinkPlugin)

plugin_pool.register_plugin(Html5UpActionLinksPlugin)


class Html5UpContainerPlugin(Html5UpPluginBase):
    name = _("Html5Up Container")
    parent_classes = None
    require_parent = False
    allow_children = True
    render_template = 'html5up_spectral_container.html'
    glossary_fields = (
        PartialFormField('heading', widgets.TextInput(attrs={}), _("Heading content")),
    )

    @classmethod
    def get_identifier(cls, instance):
        # identifier = super(HtmlFiveUpContainerPlugin, cls).get_identifier(instance)
        identifier = "Html5Up Container"
        return identifier

    def render(self, context, instance, placeholder):
        context = super(Html5UpContainerPlugin, self).render(context, instance, placeholder)
        context['heading'] = instance.glossary.get('heading', '')
        return context

plugin_pool.register_plugin(Html5UpContainerPlugin)



class Html5UpSpectralBanner(Html5UpPluginBase):
    name = _("Html5Up Spectral Banner")
    parent_classes = ('Html5UpContainerPlugin',)
    require_parent = True
    allow_children = True
    render_template = 'html5up_spectral_banner.html'
    glossary_fields = (
        PartialFormField('heading', widgets.TextInput(attrs={}), _("Banner Center Heading")),
        PartialFormField('abstract', TextEditorWidget(attrs={}), _("Banner Abstract")),
    )

    @classmethod
    def get_identifier(cls, instance):
        # identifier = super(HtmlFiveUpContainerPlugin, cls).get_identifier(instance)
        identifier = "Html5Up Spectral Banner"
        return identifier


    def render(self, context, instance, placeholder):
        context = super(Html5UpSpectralBanner, self).render(context, instance, placeholder)
        context.update({
            'heading' : instance.glossary.get('heading', ''),
            'abstract' : Html5UpSpectralBanner.unescape_html(instance.glossary.get('abstract', ''))
        })
        return context

plugin_pool.register_plugin(Html5UpSpectralBanner)



class Html5UpSpectralSpecial(Html5UpPluginBase):
    name = _("Html5Up Spectral Special")
    parent_classes = ('Html5UpContainerPlugin',)
    require_parent = True
    allow_children = True
    render_template = 'html5up_spectral_special.html'
    glossary_fields = (
        PartialFormField('heading', widgets.TextInput(attrs={}), _("Special Heading")),
        PartialFormField('abstract', TextEditorWidget(attrs={}), _("Special Abstract")),
    )

    @classmethod
    def get_identifier(cls, instance):
        # identifier = super(HtmlFiveUpContainerPlugin, cls).get_identifier(instance)
        identifier = "Html5Up Spectral Special"
        return identifier

    def render(self, context, instance, placeholder):
        context = super(Html5UpSpectralSpecial, self).render(context, instance, placeholder)
        context.update({
            'heading' : instance.glossary.get('heading', ''),
            'abstract' : Html5UpSpectralSpecial.unescape_html(instance.glossary.get('abstract', ''))
        })
        return context

plugin_pool.register_plugin(Html5UpSpectralSpecial)


class Html5UpSpectralSpotlightsForm(ManageChildrenFormMixin, ModelForm):
     num_children = IntegerField(min_value=1, initial=1,
         widget=NumberInputWidget(attrs={'size': '3', 'style': 'width: 5em !important;'}),
         label=_("Number of spotlights"),
         help_text=_("Number of spotlights"))


class Html5UpSpectralSpotlights(Html5UpPluginBase):
    name = _("Html5Up Spectral Spotlights")
    parent_classes = ('Html5UpContainerPlugin',)
    form = Html5UpSpectralSpotlightsForm
    require_parent = True
    allow_children = True
    render_template = 'html5up_spectral_spotlights.html'

    @classmethod
    def get_identifier(cls, instance):
        # identifier = super(HtmlFiveUpContainerPlugin, cls).get_identifier(instance)
        identifier = "Html5Up Spectral Spotlights"
        return identifier

    def save_model(self, request, obj, form, change):
        wanted_children = int(form.cleaned_data.get('num_children'))
        super(Html5UpSpectralSpotlights, self).save_model(request, obj, form, change)
        self.extend_children(obj, wanted_children, Html5UpSpectralSpotlight)

plugin_pool.register_plugin(Html5UpSpectralSpotlights)


class Html5UpSpectralSpotlight(Html5UpPluginBase):
    name = _("Html5Up Spectral Spotlight")
    parent_classes = ('Html5UpSpectralSpotlights',)
    require_parent = True
    allow_children = True
    alien_child_classes = True
    render_template = 'html5up_spectral_spotlight.html'
    glossary_fields = (
        PartialFormField('heading', widgets.TextInput(attrs={}), _(" Heading")),
        PartialFormField('abstract', TextEditorWidget(attrs={}), _(" Abstract")),
    )

    @classmethod
    def get_identifier(cls, instance):
        # identifier = super(HtmlFiveUpContainerPlugin, cls).get_identifier(instance)
        identifier = "Html5Up Spectral Spotlight"
        return identifier


    def render(self, context, instance, placeholder):
        context = super(Html5UpSpectralSpotlight, self).render(context, instance, placeholder)
        context.update({
            'heading' : instance.glossary.get('heading', ''),
            'abstract' : Html5UpSpectralSpecial.unescape_html(instance.glossary.get('abstract', ''))
        })
        return context

plugin_pool.register_plugin(Html5UpSpectralSpotlight)
