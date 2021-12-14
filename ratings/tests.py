from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase
from .models import Project, Profile

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
            username="test_user", first_name="mzee", last_name="mzima"
        )

        self.profile = Profile(
            bio="Test Bio",
            user=user,
            contact="Test Contact",
        )
