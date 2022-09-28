from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    task_date = models.DateField(auto_now_add = True)
    task_title = models.TextField()
    task_description = models.TextField()

class CreateTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_title', 'task_description']
