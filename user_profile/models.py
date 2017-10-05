from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserType(models.Model):
    user_type = models.CharField(max_length=100)

class UserUserType(models.Model):
    user = models.ForeignKey(User)
    user_type = models.ForeignKey(UserType)

class StudentProfile(models.Model):
    user = models.ForeignKey(User)
    mobile_number = models.CharField(max_length=20)
    student_number = models.CharField(max_length=20,null=True,blank=True)
