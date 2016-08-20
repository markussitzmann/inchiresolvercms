# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from cmsplugin_cascade.plugin_base import CascadePluginBase

from django.forms import widgets
from django.utils.translation import ugettext_lazy as _

from cmsplugin_cascade.fields import PartialFormField




from html import unescape
    
class Html5UpPluginBase(CascadePluginBase):
    module = 'Html5Up'
    require_parent = True
    allow_children = True
    render_template = 'cascade/generic/wrapper.html'

    @classmethod
    def unescape_html(cls, html_string):
        return unescape(html_string)



class Html5UpContainerPlugin(Html5UpPluginBase):
    name = _("Html5Up Container")
    parent_classes = None
    require_parent = False
    allow_children = True
    render_template = 'html5up_container.html'
#    glossary_fields = (
#        PartialFormField('heading', widgets.TextInput(attrs={}), _("Heading content")),
#    )

    @classmethod
    def get_identifier(cls, instance):
        identifier = "Html5Up Container"
        return identifier

    def render(self, context, instance, placeholder):
        context = super(Html5UpContainerPlugin, self).render(context, instance, placeholder)
#       context['heading'] = instance.glossary.get('heading', '')
        return context