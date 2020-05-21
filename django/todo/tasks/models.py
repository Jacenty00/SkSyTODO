from django.db import models

# Create your models here.
class Task(models.Model):
    task_text = models.CharField(max_length=160)
    task_progress = models.IntegerField(default=0)
    task_deadline = models.DateField()