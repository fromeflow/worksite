from django.template.loader import render_to_string

class ToLinkMixin(object):
    link_icon_template = None

    def link_icon_str(self):
        return self.link_str()

    def link_str(self):
        return str(self)

    def to_link_icon(self):
        icon = None
        if self.link_icon_template:
            icon = render_to_string(self.link_icon_template)
        return render_to_string('to_link_icon.html', {'object': self, 'icon': icon})

    def to_link(self):
        return render_to_string('to_link.html', {'object': self})