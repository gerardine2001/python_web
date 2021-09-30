from rest_framework import serializers
from student.models import Student
from trainer.models import Trainer
from course.models import Course

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=("first_name","last_name","age","date_of_birth","gender","email")


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trainer
        fields=("first_name","last_name","gender","nationality")  

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=("course_name","trainer","syllabus","course_duration","description")           
        
