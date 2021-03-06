from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from student.models import Student
from .serializers import StudentSerializer
from trainer.models import Trainer
from .serializers import TrainerSerializer
from course.models import Course
from .serializers import CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset=Trainer.objects.all()
    serializer_class=TrainerSerializer  

class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer    


