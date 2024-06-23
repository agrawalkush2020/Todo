from django import forms
from .models import Task


class Task_Creation_Form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['value']
