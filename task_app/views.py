from django.shortcuts import render,redirect
from django.views.generic import View,UpdateView
from task_app.forms import TaskForm
from task_app.models import Task
from django.shortcuts import get_object_or_404
# Create your views here.
class Add_task_view(View):
    def get(self,request):
        form = TaskForm()
        return render(request,"task_add.html",{"form":form})
    
    def post(self,request):
        print(request.POST)
        form =TaskForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            task =form.save(commit=False)
            task.user =request.user
            task.save()
        return render(request,"task_add.html",{"form":form})  

class Tasklistview(View):
    def get(self,request):
        task = Task.objects.filter(user=request.user)
        return render(request,"task_list.html",{"task":task})    
         
class Taskupdateview(UpdateView):
    model=Task
    form_class=TaskForm
    template_name="task_update.html"

class Taskdelete(View):
    def get(self,request,**kwargs):
        id =kwargs.get("pk")
        task =get_object_or_404(Task,id=id,user=request.user)
        task.delete()
        return redirect("signup")