from django.shortcuts import render, redirect
from .models import Task
from .forms import Task_Creation_Form

# Create your views here.


def index(request):
    if not request.user.is_authenticated():
        redirect('login')
    else:
        if request.method == 'POST':
            form = Task_Creation_Form(request.POST)
            if form.is_valid():  # True/False
                task = form.save(commit=False)
                task.user = request.user
                task.save()

        tasks = Task.objects.filter(user=request.user)
        form = Task_Creation_Form()
        return render(request, 'tasks/index.html', {'tasks': tasks, 'form': form})

