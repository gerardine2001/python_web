from django import forms
from django.forms import fields
from django.db.models.base import Model
from .models import Course

class CoursesRegistrationForm(forms.ModelForm):
    class Meta:
        model= Course
        fields="__all__"