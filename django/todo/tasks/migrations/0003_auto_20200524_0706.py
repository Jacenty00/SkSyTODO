# Generated by Django 3.0.6 on 2020-05-24 07:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_remove_task_task_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_progress',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0, 'Progress >= 0'), django.core.validators.MaxValueValidator(100, 'Progress <= 100')]),
        ),
    ]
