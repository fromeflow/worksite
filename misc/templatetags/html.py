from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='link_icon')
def link_icon(object):
    return mark_safe(object.to_link_icon())


@register.filter(name='link')
def link(object):
    return mark_safe(object.to_link())