from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from student.models import Student
from trainer.models import Trainer
from course.models import Course

def home(request):
    students=Student.objects.count()
    trainers=Trainer.objects.count()
    courses=Course.objects.count()


    data={"students":students, "trainers":trainers,"courses":courses}
    return render(request,"home.htm",data)


