from django.forms import ModelForm, TextInput, Textarea,CheckboxInput
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        exclude = ("user", "is_done")
        widgets = {
               'priority': TextInput(attrs={
                'style': 'max-width: 300px;margin-left:32px;background-color:black;color :white;border-radius:5px;height:40px;',
                'placeholder': 'Priority'
                }),
                'due_date': TextInput(attrs={
                'style': 'max-width: 300px;margin-left:20px;background-color:black;color :white;border-radius:5px;height:40px',
                'placeholder': 'Due-date'
                }),
                'title': TextInput(attrs={
                'style': 'max-width: 300px;margin-left:50px;background-color:black;color :white;border-radius:5px;height:40px',
                'placeholder': 'Title'
                }),
                'description': Textarea(attrs={
                'style': 'max-width: 300px;background-color:black;color :white;border-radius:5px;height:100px;margin-top:15px',
                'placeholder': 'Description'
                }),
        }

class EditForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        exclude = ("user",)
        widgets = {
               'priority': TextInput(attrs={
                'style': 'max-width: 300px;margin-left:32px;background-color:black;color :white;border-radius:5px;height:40px;',
                'placeholder': 'Priority'
                }),
                'is_done': CheckboxInput(attrs={
                'style': 'width:30px;height:30px;backgruond-color:black;margin-left:30px',
                'placeholder': 'Priority'
                }),
                'due_date': TextInput(attrs={
                'style': 'max-width: 300px;margin-left:20px;background-color:black;color :white;border-radius:5px;height:40px',
                'placeholder': 'Due-date'
                }),
                'title': TextInput(attrs={
                'style': 'max-width: 300px;margin-left:50px;background-color:black;color :white;border-radius:5px;height:40px',
                'placeholder': 'Title'
                }),
                'description': Textarea(attrs={
                'style': 'max-width: 300px;background-color:black;color :white;border-radius:5px;height:100px;margin-top:15px',
                'placeholder': 'Description'
                }),
        }

    
