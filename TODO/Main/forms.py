from django import forms
from . import models

class Task_form(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ["name", "discription", "tags"]

        help_texts = {
            "name": "Введите своё имя ", 
            "discription": "Введите описание",
        }