from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='to_link')
def to_link(object):
    return mark_safe(object.to_link())