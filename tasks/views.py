import copy

from django.shortcuts import render, redirect
from .models import Task
from .forms import Task_Creation_Form
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == 'POST':
            form_data = copy.deepcopy(request.POST)
            form = Task_Creation_Form(form_data)
            if form.is_valid():  # True/False
                task = form.save(commit=False)
                task.user = request.user
                task.save()

        tasks = Task.objects.filter(user=request.user)
        form = Task_Creation_Form()
        return render(request, 'tasks/index.html', {'tasks': tasks})
