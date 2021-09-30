from student.models import Student
from trainer.models import Trainer
from course.models import Course
from django import urls
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import home

urlpatterns=[
    path('',home, name='home_view'),
    path('course/', Course, name='Course'),
    path('trainer/',Trainer, name='Trainer'),
    path('student/', Student, name='Student'),

]

