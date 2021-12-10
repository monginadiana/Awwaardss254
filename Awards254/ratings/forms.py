from django.forms.models import ModelForm
from .models import Profile,Project
from django.forms import ModelForm
from django import forms

class DisplayProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('image','link','name','description','category','location',
                   
        )

