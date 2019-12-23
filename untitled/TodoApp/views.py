from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import TodoApp

# Create your views here.
def todos(request):
    todos_list = TodoApp.objects.all()
    data = {
        "todos": list(todos_list.values(
            "todo", "done"
        ))
    }
    return JsonResponse(data)

def single_todo(request, pk):
    todo = get_object_or_404(TodoApp, pk=pk)
    data = {
        "todo": todo.todo,
        "done": todo.done
    }
    return JsonResponse(data)

def single_todo(request, pk):
    todo = get_object_or_404(TodoApp, pk=pk)
    data = {
        "todo": todo.todo,
        "done": todo.done
    }
    return JsonResponse(data)