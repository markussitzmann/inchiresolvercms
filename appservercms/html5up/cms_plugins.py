# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.plugin_pool import plugin_pool
from .cms_plugin.spectral import *

plugin_pool.register_plugin(Html5UpSpectralContainerPlugin)
plugin_pool.register_plugin(Html5UpSpectralBanner)
plugin_pool.register_plugin(Html5UpSpectralSpecial)
plugin_pool.register_plugin(Html5UpSpectralSpotlights)
plugin_pool.register_plugin(Html5UpSpectralSpotlight)


# class Html5UpTextPlugin(Html5UpPluginBase):
#     name = _("Html5Up Text")
#     require_parent = True
#     allow_children = False
#     render_template = 'html5up_abstract_text.html'
#     glossary_fields = (
#         PartialFormField('abstract', TextEditorWidget(),),
#     )
#
#     @classmethod
#     def get_identifier(cls, instance):
#         # identifier = super(HtmlFiveUpContainerPlugin, cls).get_identifier(instance)
#         identifier = "Html5Up Text"
#         return identifier
#
#     def render(self, context, instance, placeholder):
#         abstract = instance.glossary.get('abstract', '')
#         context.update({
#             'abstract': Html5UpTextPlugin.unescape_html(abstract),
#         })
#         return super(Html5UpTextPlugin, self).render(context, instance, placeholder)
#
# plugin_pool.register_plugin(Html5UpTextPlugin)
#
#
#
# class Html5UpActionLinksForm(ManageChildrenFormMixin, ModelForm):
#     num_children = IntegerField(min_value=1, initial=1,
#         widget=NumberInputWidget(attrs={'size': '3', 'style': 'width: 5em !important;'}),
#         label=_("Action Links"),
#         help_text=_("Number of action links"))
#
#
# class Html5UpActionLinksPlugin(Html5UpPluginBase):
#     name = _("Action Links")
#     form = Html5UpActionLinksForm
#     parent_classes = ('Html5UpFullScreenPlugin', 'Html5UpSpotlightPlugin', 'Html5UpSectionPlugin')
#     require_parent = True
#     allow_children = True
#     child_classes = None
#     render_template = 'html5up_action_link_plugin.template'
#
#
#     @classmethod
#     def get_identifier(cls, instance):
#         identifier = super(Html5UpActionLinksPlugin, cls).get_identifier(instance)
#         num_cols = instance.get_children().count()
#         content = ungettext_lazy('with {} link', 'with {} links', num_cols).format(num_cols)
#         return format_html('{0}{1}', identifier, content)
#
#     def save_model(self, request, obj, form, change):
#         wanted_children = int(form.cleaned_data.get('num_children'))
#         super(Html5UpActionLinksPlugin, self).save_model(request, obj, form, change)
#         self.extend_children(obj, wanted_children, TextLinkPlugin)
#
# plugin_pool.register_plugin(Html5UpActionLinksPlugin)




