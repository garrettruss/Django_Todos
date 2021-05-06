from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Todo


# Create your views here.

def index(request):
    return render(request, 'index.html', {
        'todos': Todo.objects.all()
    })

def about(request):
    return render(request, 'about.html')


class CreateTodo(CreateView):
    model = Todo
    fields = ['description']
    success_url = '/'

class UpdateTodo(UpdateView):
    model = Todo
    fields = ['description', 'completed']
    success_url = '/'

class DeleteTodo(DeleteView):
    model = Todo
    success_url = '/'
