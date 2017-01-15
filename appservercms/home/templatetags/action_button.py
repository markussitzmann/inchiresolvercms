from django import template
from home.models import *

register = template.Library()


@register.inclusion_tag('home/tags/action_button.html', takes_context=True)
def action_button(context, button_uuid):
    return {
        'button': EditorialActionButton.objects.get(uuid=button_uuid),
        'request': context['request'],
    }