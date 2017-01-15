from django import template
from home.models import *

register = template.Library()

@register.inclusion_tag('home/tags/action_button.html', takes_context=True)
def action_button(context, button):
    if button:
        return {
            'button': EditorialActionButton.objects.get(id=button.id),
            'request': context['request'],
        }
    else:
        return {
            'button': None,
            'request': context['request'],
        }