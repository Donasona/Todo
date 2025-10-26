from django.shortcuts import render
from django.views.generic import View
from task_app.forms import TaskForm
# Create your views here.
class Add_task_view(View):
    def get(self,request):
        form = TaskForm()
        return render(request,"task_add.html",{"form":form})
    
       