from django.forms.models import ModelForm
from .models import Profile,Project
from django.forms import ModelForm
from django import forms

class DisplayProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('image','link','name','description','category','location',
                   
        )

class   CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo','bio','contact']
