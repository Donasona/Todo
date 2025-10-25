from django import forms
from user_app.models import User
from user_app.models import Task

class Userregisterform(forms.ModelForm):
    class Meta:
        model = User
        fields =['username','first_name','last_name','password','email']

class Taskform(forms.ModelForm):
    class Meta:
        model =Task
        fields =['title']
        widgets ={'title':forms.TextInput(attrs={'placeholder':'Add a new task'})}

