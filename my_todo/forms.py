from django import forms
from django.forms import ModelForm
from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = task  #task is class in models
        fields = '__all__' #mean all fields
