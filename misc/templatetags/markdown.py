from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from markdown import markdown

register = template.Library()


@register.filter(name='markdown')
@stringfilter
def to_markdown(value):
    return mark_safe(markdown(value, output_format='html5', safe_mode='escape'))