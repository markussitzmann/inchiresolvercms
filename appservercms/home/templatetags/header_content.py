from django import template
from home.models import *

register = template.Library()

@register.inclusion_tag('home/tags/header_content.html', takes_context=True)
def header_content(context, header):
    if header:
        return {
            'header_content': EditorialHeader.objects.get(id=header.id),
            'request': context['request'],
        }
    else:
        return {
            'header_content': None,
            'request': context['request'],
        }