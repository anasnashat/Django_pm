from django import forms
from . import models


class ProjectCreatForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ["title", "description", "category"]
        widgets = {
            'title': forms.TextInput(),
            'description': forms.Textarea(),
            'category': forms.Select(),
        }
