from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .serializers import TaskSerializer
from .forms import TaskForm

# API ViewSet (already implemented)
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# List View (to display all tasks)
def task_list_view(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Details View (to display details of a single task)
def task_detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

# Add/Edit View (to add a new task or edit an existing one)
def task_form_view(request, pk=None):
    if pk:
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task)
    else:
        form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task if pk else None)
        if form.is_valid():
            form.save()
            return redirect('task_list')

    return render(request, 'tasks/task_form.html', {'form': form})

# Delete View (to delete a task)
def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
