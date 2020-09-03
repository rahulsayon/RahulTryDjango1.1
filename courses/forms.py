
from  django import forms
from courses.models import Course


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title'
        ]
    
    def clean_title(self,*args,**kwargs):
        title = self.cleaned_data.get('title')
        if title.lower() == "abc":
            raise forms.ValidationError("This title is already Taken")
        else:
            return title