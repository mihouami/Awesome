from django.forms import ModelForm
from .models import *
from django import forms

class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['url', 'body', 'tags']
        labels = {
            'body' : 'Caption',
            'tags' : 'Category',
        }
        widgets = {
            'url' : forms.TextInput(attrs={'placeholder':'Add url...'}),
            'body' : forms.Textarea(attrs={'rows':3, 'placeholder':'Add a Caption...', 'class':'font1 text-4xl'}),
            'tags' : forms.CheckboxSelectMultiple(),
            
        }
        
        
class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'tags']
        labels = {
            'body' : '',
            'tags' : 'Category',
        }
        widgets = {
            'body' : forms.Textarea(attrs={'rows':3, 'class':'font1 text-4xl'}),
            'tags' : forms.CheckboxSelectMultiple(),
        }
