from django.template.loader import render_to_string


class ToLinkMixin(object):
    link_icon_class = None

    def link_str(self):
        return str(self)

    def to_link_icon(self):
        return render_to_string('misc/to_link_icon.html', {'object': self})

    def to_link(self):
        return render_to_string('misc/to_link.html', {'object': self})