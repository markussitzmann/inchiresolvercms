from django import template
from home.models import *

register = template.Library()

@register.inclusion_tag('home/tags/action_buttons.html', takes_context=True)
def action_buttons(context):
    return {
        'buttons': EditorialActionButton.objects.all(),
        'request': context['request'],
    }