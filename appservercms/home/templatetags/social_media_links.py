from django import template
from home.models import *

register = template.Library()


# Advert snippets
@register.inclusion_tag('home/tags/social_media_links.html', takes_context=True)
def socialmedialinks(context):
    return {
        'links': SocialMediaLink.objects.all(),
        'request': context['request'],
    }