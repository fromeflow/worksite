from django.forms import ModelForm, Textarea, TextInput

from .models import Course, CourseVersion


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'abbreviation', 'specialty', 'chair', 'closed', 'description']
        widgets = {
            'title': TextInput(attrs={'size': '70'}),
            'description': Textarea(attrs={'data-uk-htmleditor': '{markdown:true}'}),
        }

class CourseVersionForm(ModelForm):
    # TODO Фильтровать группы по специальности
    class Meta:
        model = CourseVersion
        fields = ['group', 'description', 'syllabus']
        widgets = {
            'description': Textarea(attrs={'data-uk-htmleditor': '{markdown:true}'}),
        }