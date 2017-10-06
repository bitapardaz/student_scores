from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images',null=True,blank=True)

class StudentCourseScore(models.Model):
    student = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    score = models.IntegerField(default=100)
    valid_until = models.DateTimeField()
    test_field = models.IntegerField(default=0)
