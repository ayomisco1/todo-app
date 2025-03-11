from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Todo

# Create your views here.
def list_todo(request):
    # Views to list all todos

    todos  = Todo.objects.all()

    templates = loader.get_template('index.html')
    context = {
        'todo_list': todos
    }

    return HttpResponse(templates.render(context, request))


    

  