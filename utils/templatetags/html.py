from markdown import markdown as md
from markdown.extensions.toc import TocExtension
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.tables import TableExtension

from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
def link_icon(object):
    return mark_safe(object.to_link_icon())


@register.filter
def link(object):
    return mark_safe(object.to_link())

@register.filter
@stringfilter
def markdown(value, header_level=1):
    html = md(value,
              output_format='html5', safe_mode='escape',
              extensions=[
                  TocExtension(baselevel=header_level),
                  CodeHiliteExtension(),
                  FencedCodeExtension(),
                  TableExtension(),
              ])
    return mark_safe(html)

