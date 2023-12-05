from django.forms import ModelForm
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        exclude = ("user", "is_done",)


class EditForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        exclude = ("user",)

    
