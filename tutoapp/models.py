from django.contrib.auth.models import User
from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  
  def __str__(self):
    return self.firstname
    

class Details(models.Model):
  member = models.ForeignKey(Member, on_delete=models.CASCADE)
  description = models.TextField()
  age = models.IntegerField()
  sex = models.CharField(max_length=10)
  education = models.CharField(max_length=100)
  hobbies = models.CharField(max_length=255)
  image = models.ImageField(upload_to='details_images/', blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"Details of {self.member.firstname} {self.member.lastname}"