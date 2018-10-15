from django.views.generic import ListView, DetailView
from .models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


class TaskListView(ListView):
    model = Task
    template_name = 'home.html'




class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_new.html'
    fields = '__all__'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_edit.html'
    fields = ['title']


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    context_object_name = 'task_detail'
    success_url = reverse_lazy('home')
