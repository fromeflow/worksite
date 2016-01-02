from django.forms import ModelForm, Textarea, TextInput

from .models import Textbook

class TextbookForm(ModelForm):
    class Meta:
        model = Textbook
        fields = ['authors', 'is_compiler', 'title', 'publisher', 'year', 'courses', 'description']
        widgets = {
            'title': TextInput(attrs={'size': '200'}),
            'description': Textarea(attrs={'data-uk-htmleditor': '{markdown:true}'}),
        }