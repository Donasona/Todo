from django.shortcuts import render
from django.views.generic import View
from task_app.forms import TaskForm
from task_app.models import Task
# Create your views here.
class Add_task_view(View):
    def get(self,request):
        form = TaskForm()
        return render(request,"task_add.html",{"form":form})
    
    # def post(self,request):
    #     print(request.POST)
    #     form =TaskForm(request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         task =form.save(commit=False)
    #         task.user =request.user
    #         task.save()
    #     return render(request,"task_add.html",{"form":form})       