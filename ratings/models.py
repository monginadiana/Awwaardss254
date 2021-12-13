from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models


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

  # search project using project name
    @classmethod
    def search_project_name(cls, search_term):
        images = cls.objects.filter(name__icontains=search_term)
        return images    

    def str(self):
        return self.user.username

# rating models
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design_rate = models.IntegerField(default=0, blank=True, null=True)
    usability_rate = models.IntegerField(default=0, blank=True, null=True)
    content_rate = models.IntegerField(default=0, blank=True, null=True)
    avg_rate = models.IntegerField(default=0, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def save_rating(self):
        self.save()

    def delete_rating(self):
        self.delete()

    @classmethod
    def filter_by_id(cls, id):
        rating = Rating.objects.filter(id=id).first()
        return rating

    def __str__(self):
        return self.user.username
    
