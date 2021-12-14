from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Project, Profile,Rating

# Create your tests here.


class ProjectTestClass(TestCase):  # Project class test
    def setUp(self):
        # create a user
        user = User.objects.create(
            username="test_user", first_name="diana", last_name="mongina"
        )

        self.project = Project(
            name="Test Project",
            description="Test Description",
            image="image.jpg",
            user=user,
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))
    
    
    def test_save_method(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)
    
    def test_delete_method(self):
        self.project.save_project()
        self.project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 0)
        
class ProfileTestClass(TestCase):  # Profile class test
    def setUp(self):
        # create a user
        user = User.objects.create(
            username="test_user", first_name="diana", last_name="mongina"
        )

        self.profile = Profile(
            bio="Test Bio",
            user=user,
            contact="Test Contact",
        )
    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))
    
    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    
    
    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)
    
          
class RatingTestClass(TestCase):  # Rating class test
    def setUp(self):
        # create a user
        user = User.objects.create(
            username="test_user", first_name="diana", last_name="mongina"
        )

        self.ratings = Rating(
            design_rate="2",
            user=user,
            content_rate="3",
        )
        
    def test_save_method(self):
        self.ratings.save_rating()
        rating = Rating.objects.all()
        self.assertTrue(len(rating) > 0)