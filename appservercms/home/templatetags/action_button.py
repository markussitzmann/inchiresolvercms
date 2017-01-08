from django import template
from home.models import *

register = template.Library()


# Advert snippets
@register.inclusion_tag('home/tags/action_buttons.html', takes_context=True)
def actionbuttons(context):
    return {
        'buttons': EditorialActionButton.objects.all(),
        'request': context['request'],
    }