# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from cmsplugin_cascade.plugin_base import CascadePluginBase

#from html.parser import HTMLParser
from html import unescape
    
class Html5UpPluginBase(CascadePluginBase):
    module = 'Html5Up'
    require_parent = True
    allow_children = True
    render_template = 'cascade/generic/wrapper.html'

    @classmethod
    def unescape_html(cls, html_string):
        #html_parser = HTMLParser()
        return unescape(html_string)