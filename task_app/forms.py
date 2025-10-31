from django import forms
from task_app.models import Task
# from user_app.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model =Task
        fields = ["task","priority"]


    

