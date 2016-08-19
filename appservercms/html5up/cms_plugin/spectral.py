from __future__ import unicode_literals
from django.forms import widgets
from django.utils.translation import ugettext_lazy as _
from django.forms.models import ModelForm
from django.forms.fields import IntegerField

from cmsplugin_cascade.widgets import NumberInputWidget
from cmsplugin_cascade.forms import ManageChildrenFormMixin
from cmsplugin_cascade.fields import PartialFormField
#from cmsplugin_cascade.link.cms_plugins import TextLinkPlugin

from djangocms_text_ckeditor.widgets import TextEditorWidget

from .base import Html5UpPluginBase


class Html5UpSpectralContainerPlugin(Html5UpPluginBase):
    name = _("Html5Up Spectral Container")
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
        context = super(Html5UpSpectralContainerPlugin, self).render(context, instance, placeholder)
        context['heading'] = instance.glossary.get('heading', '')
        return context




class Html5UpSpectralBanner(Html5UpPluginBase):
    name = _("Html5Up Spectral Banner")
    parent_classes = ('Html5UpSpectralContainerPlugin',)
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




class Html5UpSpectralSpecial(Html5UpPluginBase):
    name = _("Html5Up Spectral Special")
    parent_classes = ('Html5UpSpectralContainerPlugin',)
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



class Html5UpSpectralSpotlightsForm(ManageChildrenFormMixin, ModelForm):
     num_children = IntegerField(min_value=1, initial=1,
         widget=NumberInputWidget(attrs={'size': '3', 'style': 'width: 5em !important;'}),
         label=_("Number of spotlights"),
         help_text=_("Number of spotlights"))


class Html5UpSpectralSpotlights(Html5UpPluginBase):
    name = _("Html5Up Spectral Spotlights")
    parent_classes = ('Html5UpSpectralContainerPlugin',)
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

