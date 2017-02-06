from django import template
from home.models import *

register = template.Library()

@register.inclusion_tag('home/tags/social_media_links.html', takes_context=True)
def social_media_links(context, page):
    return {
        'links': EditorialSocialMediaLink.objects.filter(social_media_link_placement__page=page),
        'request': context['request'],
    }

@register.inclusion_tag('home/tags/social_media_header_links.html', takes_context=True)
def social_media_header_links(context, parent):
    return {
        'links': EditorialSocialMediaLink.objects.filter(social_media_link_header_placement__parent=parent),
        'request': context['request'],
    }
