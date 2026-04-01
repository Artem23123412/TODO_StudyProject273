from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.TextField(max_length=42, verbose_name="Имя задачи")
    discraption = models.TextField(max_length=700, null = True, verbose_name="Описание задачи")
    text = models.JSONField(null = True, verbose_name="Теги")
    progress = models.IntegerField(default=0, verbose_name="Прогресс")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор задачи")
