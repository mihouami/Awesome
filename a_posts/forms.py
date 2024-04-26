from django.forms import ModelForm
from .models import *
from django import forms

class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {
            'body' : 'Caption'
        }
        widgets = {
            'body' : forms.Textarea(attrs={'rows':3, 'placeholder':'Add a Caption...', 'class':'font1 text-4xl'})
        }
