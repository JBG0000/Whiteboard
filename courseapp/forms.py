from django.forms import ModelForm
from django import forms

from courseapp.models import Course


class CourseCreationForm(ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'image', 'classnumber']