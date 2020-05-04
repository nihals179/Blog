from django import forms
from .import models

class Blogform(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields={'Paragraph','title'}