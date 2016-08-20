# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.plugin_pool import plugin_pool

from .cms_plugin.base import *
from .cms_plugin.spectral import *
from .cms_plugin.phantom import *
from .cms_plugin.phantom_article_tile import *

plugin_pool.register_plugin(Html5UpContainerPlugin)
plugin_pool.register_plugin(Html5UpSpectralBanner)
plugin_pool.register_plugin(Html5UpSpectralSpecial)
plugin_pool.register_plugin(Html5UpSpectralSpotlights)
plugin_pool.register_plugin(Html5UpSpectralSpotlight)

plugin_pool.register_plugin(Html5UpPhantomArticleTile)
plugin_pool.register_plugin(TestImagePlugin)






