from django.forms import ModelForm


class ModelForm(ModelForm):
    error_css_class = 'has-error'
    required_css_class = 'text-info'

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        # adding css classes to widgets without define the fields:
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def as_div(self):
        return self._html_output(
            normal_row=u'<div class="form-group"><div%(html_class_attr)s>%(label)s %(field)s %(help_text)s %(errors)s</div></div>\n',
            error_row=u'<div class="has-error">%s</div>',
            row_ender='</div>',
            help_text_html=u'<p class="help-block">%s</p>',
            errors_on_separate_row=False)
