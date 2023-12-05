from .models import Task
from django.views.generic import TemplateView, ListView, DetailView,CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import EditForm, TaskForm
# Create your views here.

class HomePageView(TemplateView):
    template_name = "tasks/homepage.html"

class ModelTaskDetail(ListView):
    model = Task
    template_name = "tasks/all_tasks.html"

class TaskCreate(CreateView):
    form_class = TaskForm 
    template_name = 'tasks/create.html'
    success_url = reverse_lazy("alltasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskDetail(DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = 'task'     

class EditTask(UpdateView):
    form_class = EditForm
    model = Task
    template_name = "tasks/task_edit.html"
    success_url = reverse_lazy("alltasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form) 

class DeleteTask(DeleteView):
    model = Task
    template_name = "tasks/task_delete.html"
    success_url = reverse_lazy("alltasks")    
   
    

