from django.urls import path
from  django.conf.urls import url
from .views  import student_list
from .views import register_student,student_profile,edit_student


# from .import views
urlpatterns = [
     
    path("register/",register_student,name="register_student"),
    path("list/", student_list, name = "student_list"),
    path("profile/<int:id>/",student_profile, name="student_profile"),
    path("edit/<int:id>",edit_student, name="edit_student")
    
]
