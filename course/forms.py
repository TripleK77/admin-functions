
from django import forms
from .models import Teacher
class TeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=['name','email','phone','address','education','teach_courses']
        widgets={
            'teach_courses':forms.CheckboxSelectMultiple()
        }