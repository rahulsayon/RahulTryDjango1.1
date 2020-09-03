from django import forms
from .models import Article

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if 'Rahul' in title:
            raise forms.ValidationError("Please put different Title")
        else:
            return title