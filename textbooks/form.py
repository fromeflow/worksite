from django.forms import ModelForm, Textarea, TextInput

from .models import Textbook, TextbookFile

class TextbookForm(ModelForm):
    class Meta:
        model = Textbook
        fields = ['authors', 'is_compiler', 'title', 'publisher', 'year', 'courses', 'description']
        widgets = {
            'title': TextInput(attrs={'size': '200'}),
            'description': Textarea(attrs={'data-uk-htmleditor': '{markdown:true}'}),
        }

class TextbookFileForm(ModelForm):
    class Meta:
        model = TextbookFile
        fields = ['title', 'file', 'description']
        widgets = {
            'title': TextInput(attrs={'size': '200'}),
            'description': Textarea(attrs={'data-uk-htmleditor': '{markdown:true}'}),
        }