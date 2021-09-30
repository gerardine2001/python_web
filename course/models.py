from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=12, null=True)
    trainer=models.CharField(max_length=20, null=True)
    syllabus=models.TextField(max_length=800 ,null=True)
    course_duration=models.PositiveSmallIntegerField(null=True)
    course_code=models.CharField(max_length=12, null=True)
    description=models.TextField(null=True)
