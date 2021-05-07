from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import Todo


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)
    else:
        todos = None
    return render(request, 'index.html', {
        #'todos': Todo.objects.all() all todos for all users
        'todos' : todos
    })

def about(request):
    return render(request, 'about.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # similar to req.body
        if form.is_valid():
            form.save()  # similar to Mongoose  https://mongoosejs.com/
            return redirect('index')
        # else:
            # return redirect('signup')
    else:
        # give the user a fresh form to fill out
        form = UserCreationForm()
    return render(request, "signup.html", {'form': form })

class CreateTodo(CreateView, LoginRequiredMixin):
    model = Todo
    fields = ['description']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
class UpdateTodo(UpdateView, LoginRequiredMixin):
    model = Todo
    fields = ['description', 'completed']
    success_url = '/'

class DeleteTodo(DeleteView, LoginRequiredMixin):
    model = Todo
    success_url = '/'
