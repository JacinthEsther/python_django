from django import forms

from todos.models import Mytodo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Mytodo
        fields = ['task',]