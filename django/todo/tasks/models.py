from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=30) ## Nazwa taska, to o czym ten gosciu gadal ostatnio albo zostawic ID.
    task_text = models.CharField(max_length=160)
    task_progress = models.IntegerField(default=0)
    task_deadline = models.DateField()