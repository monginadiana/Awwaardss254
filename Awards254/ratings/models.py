from django.db import models
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = CloudinaryField('image')
    bio = models.TextField(max_length=500, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)


    def save_profile(self):
        self.save() 

    def update_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile
    

    def str(self):
        return self.user.username

class Project(models.Model):
    image = CloudinaryField('image')
    link = models.URLField(max_length=255, null=True)
    name = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=250, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    category = models.TextField(max_length=20)
    location = models.TextField(max_length=20)
    technologies = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts",null=True)
    
    def save_project(self):
        self.save()
     
    def delete_project(self):
        self.delete()

    @classmethod
  # search project using project name
    def search_project_name(cls, search_term):
        projects = cls.objects.filter(
        name__icontains=search_term)
        return projects   

    def str(self):
        return self.name