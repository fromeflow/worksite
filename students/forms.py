from misc.forms import ModelForm
from students.models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student

