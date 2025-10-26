from django import forms
from task_app.models import Task

class Taskform(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["user","task","created_data","is_completed","priority"]