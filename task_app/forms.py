from django import forms
from task_app.models import Task
# from user_app.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model =Task
        fields = ["task","priority"]


# class TaskForm(forms.Form):
#     task = forms.CharField(
#         max_length=100,
#         label="Task",
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter task name'
#         })
#     )

#     PRIORITY_CHOICES = [
#         ('high', 'High'),
#         ('low', 'Low'),
#     ]
#     priority = forms.ChoiceField(
#         choices=PRIORITY_CHOICES,
#         label="Priority",
#         widget=forms.Select(attrs={
#             'class': 'form-select'
#         })
#     )

#     is_completed = forms.BooleanField(
#         required=False,
#         label="Completed",
#         widget=forms.CheckboxInput(attrs={
#             'class': 'form-check-input'
#         })
#     )


    

