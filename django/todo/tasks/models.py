from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Task(models.Model):
    task_text = models.CharField(max_length=160)
    task_progress = models.IntegerField(default=0, validators=[MinValueValidator(0, 'Progress >= 0'), MaxValueValidator(100, 'Progress <= 100')])
    task_deadline = models.DateField()