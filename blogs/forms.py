from django import forms

from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'text')
        title = {'title':forms.CharField(max_length=40)}
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
        
