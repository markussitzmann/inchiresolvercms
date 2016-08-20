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

from cmsplugin_cascade.fields import PartialFormField

from .base import Html5UpPluginBase


class Html5UpPhantomArticleTile(Html5UpPluginBase):
    name = _("Html5Up Phantom Article Tile")
    parent_classes = ('Html5UpContainerPlugin',)
    require_parent = True
    allow_children = True
    alien_child_classes = True
    render_template = 'html5up_phantom_article_tile.html'
    glossary_fields = (
        PartialFormField('heading', widgets.TextInput(attrs={}), _("Heading")),
        PartialFormField('abstract', TextEditorWidget(attrs={}), _("Abstract")),
    )

    @classmethod
    def get_identifier(cls, instance):
        # identifier = super(HtmlFiveUpContainerPlugin, cls).get_identifier(instance)
        identifier = "Html5Up Phantom Article Tile"
        return identifier


    def render(self, context, instance, placeholder):
        context = super(Html5UpPhantomArticleTile, self).render(context, instance, placeholder)
        context.update({
            'heading' : instance.glossary.get('heading', ''),
            'abstract' : Html5UpPhantomArticleTile.unescape_html(instance.glossary.get('abstract', '')),
            'test': "TEST"
        })
        return context

