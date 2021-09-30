from django.db import models
# Create your models here.


class Student(models.Model):
    def full_name(self):
        return f"{self.first_name}{self.last_name}"
    first_name = models.CharField(max_length=12, blank=True, null=True)
    last_name = models.CharField(max_length=12, null=True)
    age = models.PositiveSmallIntegerField(null=True)
    picture = models.ImageField(upload_to="images/", null=True)
    date_of_birth = models.DateField(null=True)
    email = models.EmailField(max_length=30, null=True)
    Gender_choices = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'))
    gender = models.CharField(
        max_length=30, choices=Gender_choices, default="Female", null=True)
    student_id = models.PositiveSmallIntegerField(null=True)
    Nationality = (
        ('Rwandan', 'Rwandan'),
        ('Ugandan', 'Ugandan'),
        ('Kenyan', 'Kenyan'))
    nationality = models.CharField(
        max_length=18, choices=Nationality, null=True)
    nationality_id = models.CharField(max_length=20, null=True)
    medical_report = models.FileField(upload_to="documents/", null=True)
    lanquage = models.CharField(max_length=20, null=True)
    laptop_serial_number = models.CharField(max_length=18, null=True)
    date_of_enrollment = models.DateField(null=True)
