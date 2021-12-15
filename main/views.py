from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from.models import Todo
from django.utils import timezone
# Create your views here.
def homepage(request):
    return render(request=request, 
                  template_name='main/home.html',
                  context={"tasks": Todo.objects.all})

def addtask(request):
     x = request.POST['content']
     new_task = Todo(task = x,date = timezone.now())
     new_task.save()
     return HttpResponseRedirect('..')

def removetask(request,i):
    y = Todo.objects.get(id = i)
    y.delete()
    return HttpResponseRedirect('../..')