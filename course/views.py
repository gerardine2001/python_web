from django.shortcuts import render
from django.shortcuts import redirect,render
from .models import Course

# Create your views here.
from .forms import CoursesRegistrationForm

def register_courses(request):
    if request.method=="POST":
        form= CoursesRegistrationForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            return redirect('register_course')
        else:
            print(form.errors)
    else:
        form= CoursesRegistrationForm()
    return render(request,'register_courses.htm',{"form":form})

def course_list(request):
    courses = Course.objects.all()    
    return render(request,"courses_list.htm",{"courses":courses})


    
