from . import models, forms
from django.db.models import Q, Count, QuerySet

def get_filter_task(user: models.User, progress = 0, tag = "my_tasks"):
    list_task = tasks.filter(Q(progress=progress) & Q(tag=tag))
    return list_task

def get_statistical(user: QuerySet):
    tasks = user.prefetch_related("task").get(id=2)
    counts = tasks.task.aggregate(
        count_0=Count("progress", filter=Q(progress=0)),
        count_1=Count("progress", filter=Q(progress=1)),
        count_2=Count("progress", filter=Q(progress=2)),
        count_3=Count("progress", filter=Q(progress=3)),
        count_4=Count("progress", filter=Q(progress=4)),
    )
    return counts

def readTasks(progress = 0, tag = "my_tasks"):
    tasks = filter_task()
    return tasks

def updateTask(request, id):
    if request.method == "GET":
        id = request.GET.get("id")
        task = models.Task.objects.get(id = id)
        form = forms.Task_form(data=task)
        return form
    elif request.metod == "POST":
        form = forms.Task_form(data=request.POST)
        if form.is_valid():
            form.save()
            return True
        return False
    return None

def createTask(request):
    if request.method == "GET":
        form = forms.Task_form()
        return form
    elif request.metod == "POST":
        form = forms.Task_form(data=request.POST)
        if form.is_valid():
            form.save()
            return True
        return False
    return None





# list_task = models.Task.objects.filter(progress = progress)
#     list_task = list_task.filter(tag=tag)
#     return list_task