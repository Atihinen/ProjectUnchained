from django.test import TestCase
from django.core.exceptions import ValidationError
from utils.testhelper import validate
from models import Project
from django.contrib.auth.models import User
# Create your tests here.

class ProjectTestCase(TestCase):
    
    def setUp(self):
        self.user1 = User.objects.create(username="user1", password="passwd", email="user1@test.fi")
        self.user1.save()
        self.user2 = User.objects.create(username="user2", password="passwd", email="user2@test.fi").save()
        self.project1 = Project(project_name="Project 1")
        self.project1.save()
        self.project1.members.add(self.user1)
    
    def test_project1_should_have_user1_as_member(self):
        self.assertTrue(len(self.project1.members.all()) == 1)
