from django.views.generic.edit import CreateView
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
