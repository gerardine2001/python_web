from django.db import models
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    name=models.CharField(max_length=300)
    Description=models.TextField()
    start_at=models.DateTimeField(default=timezone.now)
    close_at=models.DateTimeField(default=timezone.now)
    created_at=models.DateTimeField(default=timezone.now)
    
