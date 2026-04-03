from . import models
from django.db.models import Q

def filter_progress(progress = 0, tag = "my_tasks"):
    list_task = models.Task.objects.filter(Q(progress=progress) & Q(tag=tag))
    return list_task

# list_task = models.Task.objects.filter(progress = progress)
#     list_task = list_task.filter(tag=tag)
#     return list_task