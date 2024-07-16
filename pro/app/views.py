# from django.shortcuts import render, redirect
# from .forms import GeeksForm
# from .models import Task

# # Mapping of integer status values to their string representations
# STATUS_MAP = {
#     1: "Complete",
#     2: "Not Complete",
#     3: "Progress"
# }

# def index(request):
#     tasks = Task.objects.all()
#     # Adding a status_display attribute to each task for displaying the string representation
#     for task in tasks:
#         task.status_display = STATUS_MAP.get(task.status, "Unknown")
#     return render(request, "index.html", {'tasks': tasks})

# def add(request):
#     if request.method == "POST":
#         form = GeeksForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = GeeksForm()
#     return render(request, "add.html", {'form': form})


# from django.shortcuts import render, redirect
# from .forms import TaskForm, StatusForm
# from .models import Task, Status

# # Mapping of integer status values to their string representations
# STATUS_MAP = {
#     1: "Complete",
#     2: "Not Complete",
#     3: "Progress"
# }

# def index(request):
#     tasks = Task.objects.all()
#     # Create a dictionary to hold task and its latest status
#     task_status_list = []
#     for task in tasks:
#         latest_status = Status.objects.filter(task=task).last()
#         status_display = STATUS_MAP.get(latest_status.status, "Unknown") if latest_status else "No Status"
#         task_status_list.append({
#             'task': task,
#             'status_display': status_display
#         })
#     return render(request, "index.html", {'task_status_list': task_status_list})

# def add(request):
#     if request.method == "POST":
#         task_form = TaskForm(request.POST)
#         status_form = StatusForm(request.POST)
#         if task_form.is_valid() and status_form.is_valid():
#             task = task_form.save()
#             status = status_form.save(commit=False)
#             status.task = task
#             status.save()
#             return redirect('index')
#     else:
#         task_form = TaskForm()
#         status_form = StatusForm()
#     return render(request, "add.html", {'task_form': task_form, 'status_form': status_form})





from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm, StatusForm
from .models import Task, Status

# Mapping of integer status values to their string representations
STATUS_MAP = {
    1: "Complete",
    2: "Not Complete",
    3: "Progress"
}

def index(request):
    tasks = Task.objects.all()
    # Create a dictionary to hold task and its latest status
    task_status_list = []
    for task in tasks:
        latest_status = Status.objects.filter(task=task).last()
        status_display = STATUS_MAP.get(latest_status.status, "Unknown") if latest_status else "No Status"
        task_status_list.append({
            'task': task,
            'status_display': status_display
        })
    return render(request, "index.html", {'task_status_list': task_status_list})

def add(request):
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        status_form = StatusForm(request.POST)
        if task_form.is_valid() and status_form.is_valid():
            task = task_form.save()
            status = status_form.save(commit=False)
            status.task = task
            status.save()
            return redirect('index')
    else:
        task_form = TaskForm()
        status_form = StatusForm()
    return render(request, "add.html", {'task_form': task_form, 'status_form': status_form})

def update(request, id):
    task = get_object_or_404(Task, id=id)
    latest_status = Status.objects.filter(task=task).last()

    if request.method == "POST":
        task_form = TaskForm(request.POST, instance=task)
        status_form = StatusForm(request.POST, instance=latest_status)
        if task_form.is_valid() and status_form.is_valid():
            task_form.save()
            status = status_form.save(commit=False)
            status.task = task
            status.save()
            return redirect('index')
    else:
        task_form = TaskForm(instance=task)
        status_form = StatusForm(instance=latest_status)
    return render(request, "update.html", {'task_form': task_form, 'status_form': status_form, 'task': task})
def delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('index')