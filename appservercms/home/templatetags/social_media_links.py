from django import template
from home.models import *

register = template.Library()

@register.inclusion_tag('home/tags/social_media_links.html', takes_context=True)
def social_media_links(context):
    return {
        'links': EditorialSocialMediaLink.objects.all(),
        'request': context['request'],
    }