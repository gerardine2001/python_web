from django import forms
from django.forms import fields
from django.db.models.base import Model
from .models import Student
from django.db import models
class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model= Student
        fields="__all__"