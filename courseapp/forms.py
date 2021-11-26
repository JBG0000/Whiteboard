from django.forms import ModelForm
from django import forms

from courseapp.models import Course


class CourseCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                           'style': 'height: auto;'}))

    class Meta:
        model = Course
        fields = ['title', 'image', 'content']