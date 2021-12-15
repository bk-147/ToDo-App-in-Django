
from django.db import models
from django.db.models.fields import BooleanField, CharField, DateTimeField, TextField
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    task = models.TextField()
    date = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return self.task