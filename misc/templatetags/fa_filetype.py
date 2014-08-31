from django import template
from os.path import splitext

default_filetype = 'fa-file-o'

ext_type_mapping = {
    'fa-file-archive-o': ['7z', 'zip'],
    'fa-file-pdf-o': ['pdf'],
    'fa-file-text-o': ['txt'],
    'fa-file-code-o': ['c', 'cpp', 'py', 'm', 'f90', 'cs'],
    'fa-file-image-o': ['jpg', 'jpeg'],
    'fa-file-audio-o': ['mp3', 'flac', 'spx', 'ogg'],
    'fa-file-video-o': ['webm', 'ogm', 'avi', 'mp4', 'mkv'],
    'fa-file-word-o': ['doc', 'docx', 'dot', 'dotx'],
    'fa-file-excel-o': ['xls', 'xlsx'],
    'fa-file-powerpoint-o': ['ppt', 'pptx', 'pps', 'ppsx'],
}
ext_type = {'.' + e: t for t in ext_type_mapping.keys() for e in ext_type_mapping[t]}

register = template.Library()


@register.filter(name='fa_filetype')
def to_markdown(value):
    ext = splitext(str(value))[1].lower()
    return ext_type.get(ext, default_filetype)
