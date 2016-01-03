from os.path import splitext

from django import template
from django.template.defaultfilters import stringfilter
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

register = template.Library()


def invert(exts):
    d = {}
    for file_type in exts.keys():
        for ext in exts[file_type]:
            d[ext] = file_type
    return d


FILE_TYPES_INVERTED = {
    'archive': ['.7z', '.zip', '.xz'],
    'audio': ['.mp3', '.ogg', '.spx', '.aac'],
    'code': ['.py', '.cs', '.cpp', '.pas', '.c', '.h', '.m'],
    'excel': ['.xls', '.xlsx', '.ods'],
    'image': ['.jpg', '.jpeg', '.png', '.gif'],
    'pdf': ['.pdf'],
    'powerpoint': ['.ppt', '.pptx', '.pps', '.ppsx'],
    'text': ['.txt'],
    'video': ['.avi', '.mp4', '.mkv'],
    'word': ['.doc', '.docx', '.odt', '.dot', '.dotx'],
}

FILE_TYPES = invert(FILE_TYPES_INVERTED)

@register.filter
@stringfilter
def file_icon(path):
    ext = splitext(path)[1]
    try:
        file_type = '-' + FILE_TYPES[ext]
    except KeyError:
        file_type = ''
    return mark_safe(render_to_string('file_icon.html', {'file_type': file_type}))